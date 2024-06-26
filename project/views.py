from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Project, Task, Comment, CustomUser, ProjectMember
from .forms import ProjectForm, TaskForm, CommentForm, CustomUserCreationForm

# Signup
class SignUpView(FormView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        username = form.data.get('username')
        email = form.data.get('email')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(self.request, "Username already exists..")
        elif CustomUser.objects.filter(email=email).exists():
            messages.error(self.request, "Email already exists..")
        else:
            messages.error(self.request, "Incorrect password. Please check the form and try again..")
        return super().form_invalid(form)

#Login
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('project-list')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            messages.error(request, "Username doesn't exist")
            return self.form_invalid(self.get_form())

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(self.success_url)
        else:
            messages.error(request, 'Invalid Credentials')
            return self.form_invalid(self.get_form())

# Home view redirecting to project list
def home(request):
    return redirect('project-list')

# Project views
class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'project/project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)

class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'project/project_detail.html'
    context_object_name = 'project'

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/project_form.html'
    success_url = reverse_lazy('project-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)

        ProjectMember.objects.create(project=self.object, user=self.request.user, role='Admin')

        return response

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/project_form.html'
    success_url = reverse_lazy('project-list')

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'project/project_confirm_delete.html'
    success_url = reverse_lazy('project-list')

# Task views
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'project/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)
    
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'project/task_form.html'

    def form_valid(self, form):
        project = get_object_or_404(Project, id=self.kwargs['project_id'])
        
        user = form.cleaned_data['assigned_to']
        
        ProjectMember.objects.create(project=project, user=user, role='Member')
        
        form.instance.project = project
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('project-detail', kwargs={'pk': self.kwargs['project_id']})

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'project/task_detail.html'
    context_object_name = 'task'

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'project/task_form.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        next_url = self.request.POST.get('next')
        if next_url:
            return redirect(next_url)
        else:
            return response

    def get_success_url(self):
        return reverse_lazy('task-detail', kwargs={'pk': self.object.pk})

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'project/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')

# Comment views
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'project/comment_form.html'

    def form_valid(self, form):
        form.instance.task = get_object_or_404(Task, id=self.kwargs['task_id'])
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('task-detail', kwargs={'pk': self.kwargs['task_id']})
