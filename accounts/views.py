from django.shortcuts import render, resolve_url,reverse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView

from .forms import loginForm, registerForm
User = get_user_model()

# from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

def loginView(request):
    if request.method == 'POST':
        print(request.POST)
        form = loginForm(request.POST or None)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('accounts:home'))
            else:
                return render(request, 'accounts/home.html', {
                    'message': f'Fail Login as {username}'
                })
    else:
        form = loginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))

def registerView(request):
    form = registerForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')

        try:
            user = User.objects.create_user(username, email, password)
        except:
            user = None
        
        if user != None:
            login(request, user)
            return HttpResponseRedirect(reverse('accounts:home'))
        else:
            request.session['register_error'] = 1
            if request.session['register_error'] == 2:
                return HttpResponse('<h1>Registration Error</h1>')
    return render(request, 'accounts/register.html', {'form':form})