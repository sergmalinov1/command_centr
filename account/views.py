from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from account.forms import RegistrationForm


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'account/successful.html')
    else:
        form = RegistrationForm()
    return render(request, 'account/signup.html', {'form': form})



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
