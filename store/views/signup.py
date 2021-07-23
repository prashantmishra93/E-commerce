from django.shortcuts import render, redirect
from store.models.customer import CustomerData
from django.contrib import messages
from django.contrib.auth.hashers import make_password


def signup(request):
    if request.method != 'POST':
        return render(request, 'signup.html')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        messages.success(request, 'The New User :' + " " + request.POST['first_name'] + " " + "Is Saved Successfully..!!")
        customer = CustomerData(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)

# Validation data start from here #
        value = {
            'first_name': first_name,
            'last_name':last_name,
            'phone':phone,
            'email': email
        }
        error = None
        if not first_name:
            error = "First Name must be enter"

        elif not last_name:
            error = "Last Name must be enter"

        elif CustomerData.objects.filter(phone=phone).exists():
            error = "Phone Number must be different"

        elif not phone:
            error = "Phone Number required"

        elif CustomerData.objects.filter(email=email).exists():
            error = "Email must be different"

        elif password != password2:  # it is use for password condition
            error = "Password must be same"

# Password hashing here #
        if not error:
            customer.password = make_password(customer.password)    #it is generate password as a hash type in admin view
            customer.register()
            return redirect('home')

# Validation error here #
        else:
            data= {
                'error': error,
                'values': value
            }
            return render(request, 'signup.html', data)
