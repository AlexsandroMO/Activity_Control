from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Project, Function_Collab, Collab, Status, Activity_All
from .forms import Activity_AllForm
#from apps.funcionarios.models import 
from django.shortcuts import render, get_object_or_404, redirect


@login_required
def index(request):
    return render(request,'task/index.html')


@login_required
def ativ_collab(request):

    Activity = Activity_All.objects.all()
    St = Status.objects.all()


    return render(request,'task/atividades.html', {'Activity': Activity, 'St': St})



def Edite_Status(request, id):

    #GET = dict(request.GET)
    Activity = get_object_or_404(Activity_All, pk=id)
    St = Status.objects.all()

    form = Activity_AllForm(instance=Activity)

    if (request.method == 'POST'):
        form = Activity_AllForm(request.POST, instance=Activity)
        
        if (form.is_valid()):
            Activity.save()
            return redirect('ativ_collab')
            
        else:
            return render(request, 'task/edit_status.html', {'form': form}) 

    else:
        return render(request, 'task/edit_status.html', {'form': form})

