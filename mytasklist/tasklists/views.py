from django.shortcuts import render, redirect

from django.http import JsonResponse

from django.template.response import TemplateResponse

from django.views import View

from .models import Tasks

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
        return redirect('/login/')

class Dashboard(Login, View):
    """
        autor: Carlos Arruda
        criado em: 03/2019
    """
    def get(self, request, *args, **kwargs):
        userid = request.user.id
        tasks = TasksForm()
        get_task = Tasks.objects.filter(criado_por=userid, excluido=False)
        return render(request, 'dashboard.html',  {
            'tasks': tasks,
            'get_tasks': get_task
            })

class CreateTask(Login, View):
    """
        autor: Carlos Arruda
        criado em: 03/2019
    """
    def post(self, request, *args, **kwargs):
        titulo = request.POST['titulo']
        descricao = request.POST['descricao']
        criado_por = request.user
        try:
            task = Tasks.objects.create(
                titulo=titulo,
                descricao=descricao,
                status='p',
                criado_por = criado_por
            )
            return JsonResponse({
                "sucesso": 1
            })
        except:
            return JsonResponse({
                "sucesso": 0
            })

class DeleteTask(Login, View):
    """
        autor: Carlos Arruda
        criado em: 03/2019
    """
    def post(self, request, *args, **kwargs):
        tarefa_id = request.POST['tarefa_id']
        excluido_por = request.user.id
        try:
            task = Tasks.objects.get(
                id=tarefa_id
            )
            task.excluido = True
            task.excluido_por = excluido_por
            task.save()
            return JsonResponse({
                "sucesso": 1
            })
        except:
            return JsonResponse({
                "sucesso": 0
            })

class GetEditTask(Login, View):
    """
        autor: Carlos Arruda
        criado em: 03/2019
    """
    def get(self, request, *args, **kwargs):
        tarefa_id = request.GET['tarefa_id']
        try:
            task = Tasks.objects.get(
                id=tarefa_id
            )
            return JsonResponse({
                "sucesso": 1,
                "id": task.id,
                "titulo": task.titulo,
                "descricao": task.descricao
            })
        except:
            return JsonResponse({
                "sucesso": 0
            })
import ipdb
class EditTask(Login, View):
    """
        autor: Carlos Arruda
        criado em: 03/2019
    """
    def post(self, request, *args, **kwargs):
        tarefa_id = request.POST['edittarefaid']
        titulo = request.POST['edittitulo']
        descricao = request.POST['editdescricao']
        atualizado_por = request.user.id
        ipdb.set_trace()
        try:
            task = Tasks.objects.get(
                id=tarefa_id
            )
            task.titulo = titulo
            task.descricao = descricao
            # task.atualizado_por = atualizado_por
            task.save()
            return JsonResponse({
                "sucesso": 1
            })
        except:
            return JsonResponse({
                "sucesso": 0
            })