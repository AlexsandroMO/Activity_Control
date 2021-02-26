from django.urls import path
from . import views
from . views import index, ativ_collab, Edite_Status
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('ativ_collab/', views.ativ_collab, name='ativ_collab'),
    path('edite_status/<int:id>', views.Edite_Status, name='edite_st'),

]