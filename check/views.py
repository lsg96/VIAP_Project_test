import json
from django.http import HttpResponse, request
from django.shortcuts import render

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# Create your views here.
from django.views import View

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
        pass


class PickupView(View):
    def get(self, request):
        return render(request, 'check/pickup.html')

    def post(self, request):
        # json으로 넘겨서 json으로 받아야 함
        form = json.loads(request.body)

        print('ppp', )
        print(form)

        isError = 'N'
        try:
            carno = form['cn']
            bymd = form['birth']
        except:
            isError = 'Y'

        # carno, insptype, fdate, edate, carname, isError = carInfoSearch(request)

        carno = '28어8354'
        # insptype = 'N'
        insptype = '종합검사'
        fdate = '2022-07-01'
        edate = '2022-09-01'
        carname = '아반떼'

        if isError == 'Y':
            return HttpResponse(json.dumps("{'msg':'오류발생!!'}"), content_type='application/json')
        elif isError == 'N':

            context = {'carno': carno, 'insptype': insptype, 'fdate': fdate, 'edate': edate, 'carname': carname}
            print(context)

            return HttpResponse(json.dumps(context), content_type='application/json')


def carInfoSearch(request):
    # form = request.GET.dict()
    form = json.loads(request.body)
    isError = 'N';    carno = '';      bymd = ''
    f = '';    e = '';    i = '';    c = ''

    try:
        carno = form['carno']
        bymd = form['bymd']
    except:
        isError = 'Y'

    print(carno, bymd)

    if isError == 'N':
        # carno = '28어2384'
        # bymd = '960324'

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

        else:  # 차량 검사 일자가 아닐시
            fdate = driver.find_element(By.XPATH, f"/html/body/div[4]/div/div[2]/div[1]/div/span/span[1]")
            edate = driver.find_element(By.XPATH, f"/html/body/div[4]/div/div[2]/div[1]/div/span/span[2]")

        i = insptype.text
        f = fdate.text
        e = edate.text
        c = carname.text

    return carno, i, f, e, c, isError


class Car_infoView(View):
    def get(self, request):
        return render(request, 'check/car_info.html')

    def post(self, request):
        # json으로 넘겨서 json으로 받아야 함
        form = json.loads(request.body)

        print('aaa', )
        print(form)

        isError = 'N'
        try:
            carno = form['cn']
            bymd = form['birth']
        except:
            isError = 'Y'

        carno, insptype, fdate, edate, carname, isError = carInfoSearch(request)

        carno = '28어8354'
        # insptype = 'N'
        insptype = '종합검사'
        fdate = '2022-07-01'
        edate = '2022-09-01'
        carname = '아반떼'

        if isError == 'Y':
            return HttpResponse(json.dumps("{'msg':'오류발생!!'}"), content_type='application/json')
        elif isError == 'N':

            context = {'carno': carno, 'insptype': insptype, 'fdate': fdate, 'edate': edate, 'carname': carname}
            print(context)

            return HttpResponse(json.dumps(context), content_type='application/json')


class Car_applyView(View):
    def get(self, request):
        return render(request, 'check/car_info.html')

    def post(self, request):
        tpdata = json.loads(request.body)
        print('bbb')
        print(tpdata)

        chk = 'Y'
        print(chk)
        context = {'cfmchk': chk}
        print(context)
        return HttpResponse(json.dumps(context), content_type='application/json')