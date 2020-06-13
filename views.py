from django.shortcuts import render 
from django.views.generic import View
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth import login as login_django
 

class LoginClass(View):

    templates='index.html'

    def get(self,request, *args,**kwargs,):
        if request.user.is_authenticated:
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('Dashboard:dashboard')
        return render(request, self.templates,{})

    def post(self,request, *args,**kwargs,):
        userPost=request.POST['user']
        passwordPost=request.POST['password']
        user_session = authenticate(username = userPost, password = passwordPost)
        #ACÁ LO VALIDO
        if user_session is not None:
            login_django(
                request, user_session
            )
            next_url = request.GET.get('next')
            print(user_session.username)
            if next_url:
                return redirect(next_url)
            else:
                return redirect('Dashboard:dashboard')
        else:
            self.message = 'Usuario o contraseña incorrecto'

        return render(request, self.templates,self.getContext())
    def getContext(self):
        return{
            'error':self.message,
        }



