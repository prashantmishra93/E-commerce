from django.shortcuts import render, redirect
from store.models.customer import CustomerData

def logout(request):
    request.session.clear()
    return redirect('login')