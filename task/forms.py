from django import forms
from .models import Activity_All




class Activity_AllForm(forms.ModelForm):
    class Meta:
        model = Activity_All
        fields = ('collab_name','activity_name','activity_status','activity_comments','activity_date_start','activity_date_prev','activity_date_end')

