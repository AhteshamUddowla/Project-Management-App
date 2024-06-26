from django.contrib import admin
from .models import CustomUser, Project, ProjectMember, Task, Comment

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Project)
admin.site.register(ProjectMember)
admin.site.register(Task)
admin.site.register(Comment)