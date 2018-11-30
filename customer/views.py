from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render_to_response
from django.http import HttpResponse

from customer.forms import RegistrationForm
from structure.models import Customer_Account, Country, Clan
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
    account = []
    list_of_accounts = Customer_Account.objects.filter(customer = request.user.id)

    for item in list_of_accounts:
        account_id = item.pk
        account_name = item.account_name
        world_version = item.world.name
        clan_name = "-"
        country_name = "-"



        if item.clan is not None:
            clan = Clan.objects.get(id__contains=item.clan.pk)
            clan_name = clan.clan_name

            country = Country.objects.get(id__contains=item.clan.pk)
            country_name = country.country_name

        acc = AccountView(account_id, account_name, world_version, clan_name, country_name)
        account.append(acc)

    args['accounts'] = account
    args['account_form'] = CreateAccountForm()
    args['country_form'] = CreateCountryForm()

    return render(request, 'profile/account.html', args)

class AccountView:
    account_id = 1
    country = ""
    clan = ""
    account_name = ""
    world_version = ""

    def __init__(self, account_id, account_name, world_version,  clan="-", country="-"):
        self.account_id = account_id
        self.account_name = account_name
        self.world_version = world_version
        self.country = country
        self.clan = clan




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
    if request.POST:
        form = CreateCountryForm(request.POST)
        if form.is_valid():
            new_country = form.save()

            #Создание клана
            new_clan = Clan(clan_name="TEST", country=new_country )
            new_clan.save();

            #Присвоение клана для пользователя
            user = User.objects.get(id__contains=request.user.id)
            account = Customer_Account.objects.get(customer=user.id)
            account.clan = new_clan
            account.save()

        '''new_country = form.save(commit=False)
                   user = User.objects.get(id__contains = request.user.id)           
                   account = Customer_Account.objects.filter(id__contains = user.id)
                   new_country.account_id = account[0]  #ВОД ТУТ ПРОБЛЕМА! OnetoOne/ Нужно либо добавить проверку. либо как то интерфейсно решить
                   '''
        return redirect('/customer/account/')
    return redirect('/')



    return render(request, 'profile/country.html')
