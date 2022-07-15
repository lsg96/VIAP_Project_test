import json
from datetime import date

from django.core import serializers
from django.http import HttpResponse, request
from django.shortcuts import render

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# Create your views here.
from django.views import View

from check.models import InspFee, Agent, ApplyUser, Apply, Alert, Carzipcode


class Car_deliveryView(View):
    def get(self, request):
        return render(request, 'check/car_delivery.html')

    def post(self, request):
        pass


class Car_checkView(View):
    def get(self, request):
        return render(request, 'check/car_check.html')

    def post(self, request):
        pass



class Car_confirmView(View):
    def get(self, request):
        return render(request, 'check/car_confirm.html')

    def post(self, request):
        form = json.loads(request.body)
        # print(form)
        isError = 'N'
        isExist = ApplyUser.objects.filter(carno=form['ap_carno'], apptel=form['ap_tel']).exists()

        if isExist:
            a = ApplyUser.objects.select_related().select_related().get(carno=form['ap_carno'], apptel=form['ap_tel'])
            # print(a.appid.pdate, '/', a.appid.agid.agentname)

            context = {'name': a.appname, 'carno': a.carno, 'agent':a.appid.agid.agentname, 'tel':a.apptel, 'date':a.appid.pdate, 'isError':isError}

        else:
            context = {'isError':'Y'}

        return HttpResponse(json.dumps(context), content_type='application/json')

class PickupView(View):
    def get(self, request):
        return render(request, 'check/pickup.html')

    def post(self, request):
        # json으로 넘겨서 json으로 받아야 함
        # form = json.loads(request.body)
        print('ppp', )
        insptype = ''
        isError = 'N'
        chk = 'p'

        carno, insptype, fdate, edate, carname, sido, gugun, isError = carInfoSearch(request, chk)

        if isError == 'Y':
            isError = {'isError': 'Y'}
            return HttpResponse(json.dumps(isError), content_type='application/json')
        elif isError == 'N':
            insptype = '종합검사'
            fdate = '2022-07-01'
            edate = '2022-09-01'
            carname = '아반떼'
            agentfee = '15000'

            if insptype == 'Y':
                context = {'carno': carno, 'insptype': insptype, 'fdate': fdate, 'edate': edate, 'isError':isError}
            else:
                # 검사료 조회: 차명이로 향후 배기량으로 설정
                pf = InspFee.objects.get(insptype=insptype, carname=carname)
                print(pf.fee)
                # 검사대행원 매치
                pa = Agent.objects.filter(sido=sido, gugun=gugun)
                # print(pa[0].agentname)
                json_pa = serializers.serialize('json', pa)

                context = {'carno': carno, 'insptype': insptype, 'fdate': fdate, 'edate': edate, 'carname': carname, 'fee': pf.fee, 'agentfee': agentfee, 'json_pa': json_pa, 'isError':isError}

            print(context)

            return HttpResponse(json.dumps(context), content_type='application/json')


def carInfoSearch(request, chk):
    # form = request.GET.dict()
    form = json.loads(request.body)
    print(form)

    isError = 'N';    carno = '';      bymd = ''
    f = '';    e = '';    i = '';    c = ''
    insptype =  ''
    carno = form['carno']
    bymd = form['bymd']

    try:
        URL = 'https://www.cyberts.kr/cp/pvr/cpr/readCpPvrCarPrsecResveMainView.do'

        options = Options()  # 옵션을 조정하기 위한셋팅
        # options.add_argument('--blink-settings=imagesEnabled=false') # 이미지 로딩안하게 옵션셋팅
        options.add_argument('headless')  # headless모드 브라우저가 뜨지 않고 실행됩니다.

        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # driver.implicitly_wait(time_to_wait=5) # 로딩대기 (암묵적) 최대 5초까지

        driver.get(url=URL)
        tabs = driver.window_handles
        driver.implicitly_wait(time_to_wait=5)

        driver.switch_to.window(driver.window_handles[0])
        keyword = driver.find_element(By.XPATH,
                                      "/html/body/div[1]/div[3]/form/table/tbody/tr[1]/td/ul/li/input")  # 검색 속성 찾기
        keyword.send_keys(carno)  # 검색어 입력

        keyword = driver.find_element(By.XPATH,
                                      "/html/body/div[1]/div[3]/form/table/tbody/tr[2]/td/ul/li/input")  # 검색 속성 찾기
        keyword.send_keys(bymd)  # 검색어 입력

        keyword.send_keys("\ue007")  # 검색후 enter키 입력

        msg = (driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[1]/div").text)
        # print(driver.find_element(By.XPATH,"/html/body/div[4]/div/div[2]/div[1]/div/span/p[1]/span"))

        if msg == '검사예약 진행 가능합니다. \
                    ※ 추가정보 \
                    - 검사 당일 기준 보험 미가입자는 검사를 받으실 수 없습니다.':
            keyword = driver.find_element(By.XPATH, f"/html/body/div[4]/div/div[2]/div[2]/button")  # 계속진행
            keyword.send_keys("\ue007")  # 검색후 enter키 입력 -- 다음페이지 이동

            # data1 = driver.find_element("/html/body/div[1]/div[4]/div[1]/form/table/tbody/tr[1]/td")  # 검사구분 ex)종합검사, 부하검사 같이 받아올수 있지 확인해야 하는 영역
            # data1 = driver.find_element("/html/body/div[1]/div[4]/div[1]/form/table/tbody/tr[1]/td/ul[2]/li/p/span")  # 검사구분 ex)부하검사영역 받아올수 있는지 확인해야 함

            insptype = driver.find_element(By.XPATH,
                                           f"/html/body/div[2]/div[4]/div[1]/form/table/tbody/tr[1]/td/ul[1]/li")  # 검사구분 ex)종합검사 영역
            fdate = driver.find_element(By.XPATH,
                                        f"/html/body/div[2]/div[4]/div[1]/form/table/tbody/tr[3]/td[1]/ul/li/input[1]")  # 검사기간1 (검사 만료일)
            edate = driver.find_element(By.XPATH,
                                        f"/html/body/div[2]/div[4]/div[1]/form/table/tbody/tr[3]/td[1]/ul/li/input[2]")  # 검사기간2 (검사 만료일)
            carname = driver.find_element(By.XPATH,
                                          f"/html/body/div[2]/div[4]/div[1]/form/table/tbody/tr[3]/td[2]")  # 차명

            print(insptype.text, fdate.text, edate.text, carname.text)

            i = insptype.text
            f = fdate.text
            e = edate.text
            c = carname.text

        else:  # 차량 검사 일자가 아닐시
            fdate = driver.find_element(By.XPATH, f"/html/body/div[4]/div/div[2]/div[1]/div/span/span[1]")
            edate = driver.find_element(By.XPATH, f"/html/body/div[4]/div/div[2]/div[1]/div/span/span[2]")
            f = fdate.text
            e = edate.text
            i = 'Y'
    except:
        isError = 'Y'

    print(carno, bymd)

    if chk == 'p':
        sido = form['sido']
        gugun = form['gugun']
        return carno, i, f, e, c, sido, gugun, isError
    else:
        return carno, i, f, e, c, isError


class Car_infoView(View):
    def get(self, request):
        form = request.GET.dict()
        print(form)

        if request.GET.get('sido') is not None:
            stnames = Carzipcode.objects.filter(sido=form['sido'], gugun=form['gugun'])

            json_data = serializers.serialize('json', stnames)
            print(json_data)

            return HttpResponse(json_data, content_type='application/json')
        else:
            return render(request, 'check/car_info.html')

    def post(self, request):
        # json으로 넘겨서 json으로 받아야 함
        # form = json.loads(request.body)

        print('aaa', )
        chk = 'i'

        isError = 'N'
        carno, insptype, fdate, edate, carname, isError = carInfoSearch(request, chk)

        # insptype = '종합검사'
        # fdate = '2022-07-01'
        # edate = '2022-09-01'
        # carname = '아반떼'

        if isError == 'Y':
            isError = { 'isError': 'Y'}
            return HttpResponse(json.dumps(isError), content_type='application/json')
        elif isError == 'N':
            context = {'carno': carno, 'insptype': insptype, 'fdate': fdate, 'edate': edate, 'carname': carname, 'isError':isError}
            print(context)

            return HttpResponse(json.dumps(context), content_type='application/json')


class Car_applyView(View):
    def get(self, request):
        return render(request, 'check/pickup.html')

    def post(self, request):
        form = json.loads(request.body)

        print(form)

        chk = 'Y' ; cnt = ''

        # 예약번호 생성
        td = str(date.today()).split('-')
        std = td[0] + td[1] + td[2]

        isApp = Apply.objects.first()

        f = isApp.appno[:8]
        l = int(isApp.appno[8:])

        if std == f:
            l = str(l+1)
            cnt = l.zfill(3)
        else:
            cnt = '001'

        app_no = std + cnt
        print(app_no)

        fdt = form['app_expdate'].split('~')[0]
        edt = form['app_expdate'].split('~')[1]
        print(fdt)
        agent = form['app_agent'].split('&nbsp')[0]
        ag = Agent.objects.get(agentname=agent).agid
        print(ag)

        try:
            app = Apply(
                appno=app_no,
                insptype=form['app_insptype'],
                pdate=form['app_pdate'],
                fdate=fdt,
                edate=edt,
                ptime=form['app_ptime'],
                msg=form['msg'],
                fnames=form['fnames'],
                agid_id=Agent.objects.get(agentname=agent).agid
            )
            app.save()

            appusr = ApplyUser(
                carno=form['app_carno'],
                appname=form['app_name'],
                carname=form['app_carname'],
                apptel=form['app_tel1'],
                alttel=form['app_tel2'],
                birth=form['app_bymd'],
                addr1=form['app_addr1'],
                addr2=form['app_addr2'],
                appid_id=Apply.objects.get(appno=app_no).appid
            )
            appusr.save()
        except:
            chk = 'N'

        context = {'cfmchk': chk}
        print(context)
        return HttpResponse(json.dumps(context), content_type='application/json')


class Car_alertView(View):
    def get(self, request):
        return render(request, 'check/pickup.html')

    def post(self, request):
        form = json.loads(request.body)
        print(form)

        chk = 'Y'; cnt = ''; f = ''; l = ''; first = ''    # 초기화
        isApp = ''

        # 예약번호 생성
        td = str(date.today()).split('-')
        std = 'a' + td[0] + td[1] + td[2]
        try:
            isApp = Alert.objects.first()
            print(isApp.atno)
        except:
            first = 'Y'
            cnt = '001'

        if first != 'Y':
            f = isApp.atno[:9]
            l = int(isApp.atno[9:])


        if std == f:
            l = str(l + 1)
            cnt = l.zfill(3)
        else:
            cnt = '001'

        at_no = std + cnt
        print(at_no)

        fdt = form['at_expdate'].split('~')[0]
        edt = form['at_expdate'].split('~')[1]
        print(fdt)

        at = Alert(
            atno=at_no,
            atname=form['at_name'],
            attel=form['at_tel1'],
            atfdate=fdt,
            atedate=edt,
        )
        # print(at.atno)
        at.save()


        chk = 'Y'
        context = {'cfmchk': chk}
        print(context)
        return HttpResponse(json.dumps(context), content_type='application/json')