from django.contrib import admin
from . models import Project, Collab, Function_Collab, Status, Activity_All


class ProjectAdmin(admin.ModelAdmin):
    fields = ('project_name','company','comments')
    list_display = ('project_name','company','comments','created_proj','update_proj')
    


class CollabAdmin(admin.ModelAdmin):
    fields = ('collab_name','collab_function','collab_user')
    list_display = ('collab_name','collab_function','collab_user','created_collab','update_collab')


class StatusAdmin(admin.ModelAdmin):
    fields = ('status_name',)
    list_display = ('status_name','created_st','update_st')


class Function_CollabAdmin(admin.ModelAdmin):
    fields = ('collab_name',)
    list_display = ('collab_name',)


class Activity_AllAdmin(admin.ModelAdmin):
    fields = ('collab_name','activity_name','activity_status','activity_comments','activity_date_start','activity_date_prev','activity_date_end')
    list_display = ('collab_name','activity_name','activity_status','activity_comments','activity_date_start', 'activity_date_prev', 'activity_date_end','created_ac','update_ac')



admin.site.register(Project, ProjectAdmin)
admin.site.register(Collab, CollabAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Function_Collab, Function_CollabAdmin)
admin.site.register(Activity_All, Activity_AllAdmin)
