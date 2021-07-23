from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.product import Products
from store.models.customer import CustomerData
from django.contrib.auth.hashers import check_password
from django.views import View

class Login(View):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)

        customer = CustomerData.get_customer_by_email(email)
        error = None
        if customer:
            check = check_password(password, customer.password)
            if check:
                request.session['customer'] = customer.id
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('home')
            else:
                error = "Email or Password Invalid !!"
        else:
            error = "Email or Password Invalid !!"
        return render(request, 'login.html', {'error':error})