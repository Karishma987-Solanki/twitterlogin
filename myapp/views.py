from django.shortcuts import render

# Create your views here.


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)
    return render(request, 'login.html')