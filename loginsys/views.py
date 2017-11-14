
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib import auth
from django.template.context_processors import csrf


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Don't such a user"
            return render(request, 'loginsys/login.html', args)
    else:
        return render(request, 'loginsys/login.html', args)

def logout(request):
    auth.logout(request)
    return redirect('/')
