from django.shortcuts import render, redirect

from django.template.response import TemplateResponse

from django.views import View

from .forms import TasksForm

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
            return redirect('/dashboard/')
        else:
            return TemplateResponse(request, 'login.html',{
                "erros": "Você não possui uma conta cadastrada"
            })

class Logout(Login, View):
    """
        autor: Carlos Arruda
        criado em: 03/2019
    """
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

class Dashboard(Login, View):
    """
        autor: Carlos Arruda
        criado em: 03/2019
    """
    def get(self, request, *args, **kwargs):
        tasks = TasksForm()
        return render(request, 'dashboard.html',  {'tasks': tasks})
import ipdb
class CreateTask(Login, View):
    """
        autor: Carlos Arruda
        criado em: 03/2019
    """
    def post(self, request, *args, **kwargs):
        ipdb.set_trace()
        titulo = request.POST('titulo')
        descricao = request.POST('descricao')

    pass