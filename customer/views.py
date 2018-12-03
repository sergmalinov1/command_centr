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

'''CLASS '''
class MyAccounts:
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


class MyCountry:
    country_id = 1
    country_name = ""
    num_of_accounts = 0

    def __init__(self, country_name, num_of_accounts, country_id):
        self.country_name = country_name
        self.num_of_accounts = num_of_accounts
        self.country_id = country_id


'''DEF '''

def list_of_accounts(request):
    accounts = []
    list_of_accounts = Customer_Account.objects.filter(customer=request.user.id)

    # list_of_free_accounts
    #list_of_accounts = Customer_Account.objects.filter(customer=request.user.id).filter(clan_id=None)

    for item in list_of_accounts:
        account_id = item.pk
        account_name = item.account_name
        world_version = item.world.name
        clan_name = "-"
        country_name = "-"

        if item.clan is not None:
            clan = Clan.objects.get(id__contains=item.clan.pk)
            clan_name = clan.clan_name

            country = Country.objects.get(id__contains=clan.country_id)
            country_name = country.country_name

        acc = MyAccounts(account_id, account_name, world_version, clan_name, country_name)
        accounts.append(acc)
    return accounts

def list_of_countries(request):
    countries = []
    countries_list = Country.objects.filter(customer_id=request.user.id)

    for item in countries_list:
        num_of_acc = 0
        clan_list = Clan.objects.filter(country_id=item.id)
        for clan_item in clan_list:
            acc = Customer_Account.objects.filter(clan_id=clan_item.id)
            num_of_acc = num_of_acc + acc.count()

        my_country = MyCountry(item.country_name, num_of_acc, item.id)
        countries.append(my_country)
    return countries


@csrf_exempt
def account_view(request):

    args = {}
    args['accounts'] = list_of_accounts(request)
    args['countries'] = list_of_countries(request)
    args['account_form'] = CreateAccountForm()
    args['country_form'] = CreateCountryForm()

    return render(request, 'profile/accounts.html', args)




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
    args['accounts'] = list_of_accounts(request)
    args['countries'] = list_of_countries(request)
    args['country_form'] = CreateCountryForm()
    args['clan_form'] = CreateClanForm()
    return render(request, 'profile/country.html', args)

def create_country(request):
    if request.POST:
        form = CreateCountryForm(request.POST)

        if form.is_valid():
            #Поиск связанного аккаунта
            account_number = request.POST.get('account_number')
            account = Customer_Account.objects.get(id=account_number)

            # Создание страны
            new_country = form.save(commit=False)
            user = User.objects.get(id=request.user.id)
            new_country.customer_id = user.id
            new_country.world = account.world
            form.save()

            #Создание клана
            clan_name = request.POST.get('clan_name')
            new_clan = Clan(clan_name=clan_name, country=new_country )
            new_clan.save();

            #Присвоение клана для пользователя
            account.clan = new_clan
            account.save()

        return redirect('/customer/account/')
    return redirect('/')

    return render(request, 'profile/country.html')

def country_detail_view(request, country_id=1):
    args = {}
    args['country'] = Country.objects.get(id = country_id)

    return render(request, 'profile/country_detail.html', args)

