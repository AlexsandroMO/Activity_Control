from django.test import TestCase

# Create your tests here.



#Bootstrap e django static
#https://getbootstrap.com/docs/5.0/getting-started/download/
#https://docs.djangoproject.com/en/3.1/howto/static-files/





'''{% extends  'base.html' %}
{% load crispy_forms_tags %}

{% block title %}Login{% endblock %}

{% block content %}
<div class="row">
    <div class="col-md-4 offset-md-4">
        <div class="card  auth-card">
            <div class="card-body">
                <h4 class="card-title text-center">Entrar no To Do List</h4>
        
                <form method="post">
                    {% csrf_token %}
                    <input type="hidden" name="next" value="{{ next }}">
        
                    
                    {{ form.as_p }}

                    <button type="submit" class="btn btn-primary btn-block">Entrar</button>
                </form>

                <p class="change-form-p">Quer criar uma conta? <a href="/accounts/register">Clique aqui!</a></p>
            </div>
        </div>
    </div>
</div>
{% endblock %} 


{% load crispy_forms_tags %} 
{{ form |crispy }} '''


'''{% extends 'base.html' %}
{% block main %}

<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
</form>

{%endblock %}
'''