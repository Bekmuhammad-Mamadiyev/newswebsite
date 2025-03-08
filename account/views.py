from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render



def user_login(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            print(data)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Akkountga kirildi!')
                else:
                    return HttpResponse('Akkountingiz aktiv emas')
            else:
                return HttpResponse('Parol yoki login xato')
        else:

            form = LoginForm()
            context = {
                'form':form,
            }
    return render(request, 'registration/login.html')


def dashboardview(request):
    user = request.user
    context = {
        'user':user,

    }
    return render(request, 'pages/dashboard.html', context)

def logout_view(request):
    logout(request)
    return render(request, 'registration/logged_out.html')
