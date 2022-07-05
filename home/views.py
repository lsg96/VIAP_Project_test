from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
# from join.models import Member


class IntroView(View):
    def get(self, request):
        return render(request,'intro.html')


    def post(self, request):
        pass


class AdminView(View):
    def get(self, request):
        return render(request,'admin.html')


    def post(self, request):
        pass


class HomeView(View):
    def get(self,request):
        return render(request,'index.html')

    def post(self,request):
        pass

# 로그인 처리
class LoginView(View):
     def post(self, request):
        form = request.POST.dict()
        # print(form)
        #select from Member where userid=** and passwd=**
        returnPage = '/loginfail'
        # count = Member.objects.filter(userid= form['userid'], passwd=form['passwd']).count();
        from join.models import Member
        isExisted = Member.objects.filter(userid= form['userid'], passwd=form['passwd']).exists();
        # print(count)

        # if count == 1:
        if isExisted:
            #로그인 성공시
            #세션 변수에 아이디와 id값을 저장(userinfo:'abc123|1')
            user =Member.objects.get(userid=form['userid'])
            request.session['userinfo'] =form['userid']+'|'+str(user.id)
            print(request.session['userinfo'])
            returnPage = '/'
            
        return redirect(returnPage)
    

# 로그아웃 처리
class LogoutView(View):
    def get(self, request):
        #세션변수 중에서 userinfo키만 삭제
        # if request.session.get('userinfo'):
        #     del(request.session['userinfo'])

        # 세션변수의 모든 키를 삭제
        # keys=request.session.keys()
        # for key in keys:
        #     del (request.session[key])
        #

        #세션변수
        request.session.flush()

        return redirect('/')

    def post(self, request):
        pass

#로그인 실패시 보여줄 페이지 지정
class LoginFailView(View):
    def get(self, request):
        return render(request, 'loginfail.html')
