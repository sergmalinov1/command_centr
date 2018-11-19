from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from account.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
 #   return HttpResponse("<h3>Hello world</h3>")
    return redirect ('account/login')

@csrf_exempt
def signup_view(request):
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #log user here
            login(request, user)
            return render(request, 'account/successful.html' )
    else:
        form = RegistrationForm()
    return render(request, 'account/signup.html', {'form': form, 'num_visits':num_visits}, )

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return render(request, 'account/successful.html')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form}, )

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'account/successful.html')



""" TEST
@csrf_exempt
def login(request):
    args = {}
    args['form'] = LoginForm
    return render_to_response('customerAuth/login.html', args)


#def loginVerifications(request):
 #   if request.POST:
#        form = LoginForm
#        if (form.is_valid())

   # return render_to_response('customerAuth/registration.html')
   # return redirect('/')
"""
