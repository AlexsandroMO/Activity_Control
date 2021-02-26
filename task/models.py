from django.db import models
from django.contrib.auth import get_user_model


class Project(models.Model): #Títulos de projeto

    project_name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    comments = models.TextField()
    created_proj = models.DateTimeField(auto_now_add=True)
    update_proj = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name



class Function_Collab(models.Model): #Disciplinas do Projeto

    collab_name = models.CharField(max_length=255, verbose_name='FUNÇÃO')

    def __str__(self):
        return self.collab_name



class Collab(models.Model): #Disciplinas do Projeto

    collab_name = models.CharField(max_length=255, verbose_name='NOME DO COLABORADOR')
    collab_function = models.ForeignKey(Function_Collab, on_delete=models.CASCADE, verbose_name='FUNÇÃO')
    photo = models.FileField(upload_to='uploads/photos/', blank=True, null=True, verbose_name='FOTO')
    collab_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='USUÁRIO')
    created_collab = models.DateTimeField(auto_now_add=True)
    update_collab = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.collab_name




class Status(models.Model): #Disciplinas do Projeto

    status_name = models.CharField(max_length=255)
    created_st = models.DateTimeField(auto_now_add=True)
    update_st = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status_name



class Activity_All(models.Model): #Títulos de projeto

    collab_name = models.ForeignKey(Collab, on_delete=models.CASCADE, verbose_name='NOME')
    activity_name = models.CharField(max_length=255)
    activity_status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='STATUS DA ATIVIDADE')
    activity_comments = models.TextField()
    activity_date_start = models.DateField(blank=True, null=True)
    activity_date_prev= models.DateField(blank=True, null=True)
    activity_date_end= models.DateField(blank=True, null=True)
    created_ac = models.DateTimeField(auto_now_add=True)
    update_ac = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.activity_name


