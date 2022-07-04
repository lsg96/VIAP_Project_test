import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests
# Create your views here.
from django.views import View
from django.core import serializers

from join.models import Zipcode, Member


class CheckmeView(View):
    def get(self, request):
        return render(request, 'join/checkme.html')

    def post(self, request):
        # captcha 사용시 클라이언트가 생성한 키와
        # 서버에 설정해 둔 (비밀)키등을
        # google의 siteverify에서 비교해서 인증에 성공하면
        # joinme로 redirect하고, 그렇치 않으면 다시 checkme로 return함
        SECRET_KEY ='6LdP86YgAAAAAFGOr9pFRvR5Nezc6mSUSwwRShor'
        VERIFY_URL ='https://www.google.com/recaptcha/api/siteverify'

        form = request.POST.dict()
        # 질의를 위한 질의문자열을 작성
        # ?secret =비밀키&response =클라이언트 응답키
        params ={'secret': SECRET_KEY, 'response': form['g-recaptcha']}

        #구글 recaptcha 인증사이트에 키들을 질의문자열로 보내어
        #올바른 키인지 확인하고 결과를 json으로 받아옴
        #requests.get(URL,질의문자열)
        result = requests.get(VERIFY_URL, params=params).json()

        #결과중 success가 true면 joinme로 redirect
        if result['success']:
            # 인증성공시 이름과 전화번호를 쿠키에 저장해 둠
            tokens ={'name':form['name'],'phone':form['phone']}
            #한글저장이 가능한 JSON객체 문자열로 변환
            tokens = json.dumps(tokens,ensure_ascii=True)
            # {"name": "\uc774\uc2b9\uad6c", "phone": "123213"} (이승구) 유니코드
            # print(tokens)

            #쿠키 설정없이 페이지만 전환
            # return redirect('/join/joinme')

            #쿠기 설정
            res = redirect('/join/joinme')
            # dict 객체를 쿠키에 저장해 둠 (현재 유지시간(max_age) 10분)
            # 응답 객체.set_cookie(키, 값, 유지시간)
            res.set_cookie('tokens',tokens,max_age=60*10)
            return res


        else:
            error = '자동가입 방지 인증이 실패했습니다. 다시시도하세요'
        context={'form':form,'error':error}
        return render(request, 'join/checkme.html',context)


class JoinmeView(View):
    def get(self, request):
        #쿠키에 저장된 객체를 불러올려면 request.COOKIES.get(이름)
        cookie = request.COOKIES.get('tokens')
        # print(cookie)


        # eval :문자열을 dict객체로 변환하는 함수
        try:
            return render(request, 'join/joinme.html', eval(cookie))
        except:
            return redirect('/join/agree')

    def post(self, request):
        form = request.POST.dict()
        print(form)

        email = form['email1'] + '@' + form['email2']
        mailing = True if form['mailing'] == 'yes' else False

        # 우편번호의 일련 번호를 알아내기 위해
        # zipcode에 필요한 정보를 넘겨서 조회함
        # 단, 현남면, 경기 화정동으로 검색시
        # 하나의 결과가 아닌 복수 결과가 넘어옴
        # 새로운 setZipcode 함수 덕택으로 이코드는 사용 x

        # zipcode = form['zip1']+'-'+form['zip2']
        # addrs = form['addr1'].split(' ')
        # print(addrs)
        # zip = Zipcode.objects.get(ZIPCODE=zipcode, SIDO=addrs[0], GUGUN=addrs[1], DONG=addrs[2])
        # print(zip.seq)


        # m = Member(userid=form['userid'],
        #            passwd=form['passwd'],
        #            name=form['name'],
        #            phone=form['phone'],
        #            zip=Zipcode.objects.get(seq=zip.seq),
        #            addr=form['addr2'],
        #            email=email,
        #            mailing=mailing)
        # m.save()

        m = Member(userid=form['userid'],
                   passwd=form['passwd'],
                   name=form['name'],
                   phone=form['phone'],
                   # zip=Zipcode.objects.get(seq=zip.seq),
                   zip=Zipcode.objects.get(seq=form['seq']),
                   addr=form['addr2'],
                   email=email,
                   mailing=mailing)
        m.save()

        return redirect('/join/joinok?userid='+form['userid'])


class JoinokView(View):
    def get(self, request):
        # join/joinok?userid=***
        form = request.GET.dict()

        # select * from member join zipcode on m.zipcode =z.seq
        # where m.userid = ****
        m= Member.objects.select_related().get(userid=form['userid'])
        context ={'member':m}
        return render(request, 'join/joinok.html',context)

    def post(self, request):

        pass


class AgreeView(View):
    def get(self, request):
        return render(request, 'join/agree.html')

    def post(self, request):
        pass



class ZipcodeView(View):
    def get(self, request):
        form =request.GET.dict()

        #select * from zipcode where dong = '동이름'
        #테이블 모델명.objects.get(조건): 1개의 결과값만 처리
        #테이블모델명.objects.filter(조건) : 1개이상의 결과값 처리

        #result = Zipcode.objects.get(DONG='사당동')
        # print(result.values())  #속성명으로 값 출력

        #result = Zipcode.objects.filter(DONG='사당동')
        #print(result.values())   #속성명으로 값 출력
        #
        result = Zipcode.objects.filter(DONG=form['dong'])

        #조회 결과를 JOSON 객체로 생성
        json_data =serializers.serialize('json',result)
        # print(json_data,form['dong'])


        # 생성된 JSON객체를 HTTP 응답객체로 전송
        return HttpResponse(json_data, content_type='application/json')
        # return render(request, 'join/agree.html')

    def post(self, request):
        pass


class UseridView(View):
    def get(self, request):
        #/join/userid?userid=***
        #응답 메세지 =>{'result':0또는 1}
        form = request.GET.dict()


        #select*from member where userid = ?
        count = Member.objects.filter(userid=form['userid']).count()
        # print(count)

        # 조회된 카운트를 json형식의 데이터로 생성
        # json_data ={}
        # json_data['count']=count
        json_data ={'count':count}
        #print(json_data)




        # 생성된 json데이터를 직렬화함 - 지원안됨(직렬화시 정보부족)
        #json_data = serializers.serialize('json', json_data)

       #카운트는 json.dumps함수로 간단하게 문자열로 직렬화
        return HttpResponse(json.dumps(json_data), content_type='application/json')


        # return render(request, 'join/agree.html')

    def post(self, request):
        pass