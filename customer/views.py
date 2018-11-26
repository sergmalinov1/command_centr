from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render_to_response
from django.http import HttpResponse

from customer.forms import RegistrationForm
from structure.models import Customer_Account
from structure.forms import CreateAccountForm, CreateCountryForm, CreateClanForm

def index(request):
 #   return HttpResponse("<h3>Hello world</h3>")
    return redirect ('customer/login')

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
            return render(request, 'customer/successful.html' )
    else:
        form = RegistrationForm()
    return render(request, 'customer/signup.html', {'form': form, 'num_visits':num_visits}, )

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return render(request, 'customer/successful.html')
    else:
        form = AuthenticationForm()
    return render(request, 'customer/login.html', {'form': form}, )

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'customer/successful.html')

@login_required(login_url="/customer/login/")
def profile_view(request):
    return render(request, 'profile/profile.html')

def password_reset_view(request):
    return render(request, 'customer/password_reset.html')

'''ACCOUNT '''
@csrf_exempt
def account_view(request):
    args = {}
    args['accounts'] = Customer_Account.objects.filter(customer = request.user.id)
    args['form'] = CreateAccountForm()
   # args['request'] = request.user.id
    return render(request, 'profile/account.html', args)

@csrf_exempt
def create_account_view(request):
    if request.POST:
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            user = User.objects.get(id__contains = request.user.id)
            account.customer_id = user.id
            form.save()
        return redirect('/customer/account/')
    return redirect('/')



'''COUNTRY '''
def country_view(request):
    args = {}
    args['country_form'] = CreateCountryForm()
    args['clan_form'] = CreateClanForm()
    return render(request, 'profile/country.html', args)

def create_country(request):
    return render(request, 'profile/country.html')
