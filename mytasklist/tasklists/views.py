from django.shortcuts import render

from django.views import View

from django.contrib.auth.models import User

class Login(View):
    """
        autor: Carlos Arruda
        criado em: 03/2019
    """
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        validar = User.objects.filter(email=email)
        if validar:
            return render(request, 'dashboard.html')
        else:
            return render(request, 'login.html',{
                "erros": "Você não possui uma conta cadastrada"
            })
