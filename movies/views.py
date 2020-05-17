from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView


def about(request):
    return render(request, 'films/about_us.html')

def exit(request):
    if request.POST['exit']:
        logout(request)
        return redirect('home_page_url')

class LoginView(View):

    def get(self, request):
        return render(request, 'movie/login.html')

    def post(self, request):
        nickname = request.POST['nickname']
        password = request.POST['password']
        user = authenticate(username=nickname, password=password)
        if user is not None:
            login(request, user)
        else:
            password_error = False
            login_error = not nickname in [user.username for user in User.objects.all()]
            if not login_error:
                password_error = True
            return render(request, 'movie/login.html', context={'password_error':password_error, 'login_error':login_error})
        return redirect('home_page_url')

class RegisterView(View):

    def get(self, request):
        return render(request, 'movie/register.html')

    def post(self, request):
        nickname = request.POST['nickname']
        password = request.POST['password']
        password_again = request.POST['password_again']
        mail = request.POST['mail']
        if password == password_again:
            user = User.objects.create_user(username=nickname, password=password, email=mail)
            user.save()
            login(request, user)
            return redirect('home_page_url')

