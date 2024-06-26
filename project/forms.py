from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Project, Task, Comment, CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'assigned_to', 'due_date']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['status'].initial = 'To Do'
        self.fields['priority'].initial = 'Low'

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

        self.fields['status'].widget.attrs.update({'class':'form-select'})
        self.fields['priority'].widget.attrs.update({'class':'form-select'})
        self.fields['assigned_to'].widget.attrs.update({'class':'form-select'})

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})