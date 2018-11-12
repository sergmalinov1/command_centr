from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from customerAuth.forms import LoginForm, SignUpForm


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'customerAuth/successful.html')
    else:
        form = SignUpForm()
    return render(request, 'customerAuth/signup.html', {'form': form})



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

