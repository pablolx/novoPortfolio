from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Project




class ProjetosListView(ListView):
    model = Project
    template_name = 'novoPortfolio/projetos_list.html'
    paginate_by = 12

class ProjetosCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'novoPortfolio/projetos_form.html'
    fields = ['title', 'description', 'repo_url', 'live_url', 'tech_stack', ]
    success_url = reverse_lazy('projetos_list')

class ProjetosUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'novoPortfolio/projetos_form.html'
    fields = ['title', 'description', 'repo_url', 'live_url', 'tech_stack', ]
    success_url = reverse_lazy('projetos_list')

class ProjetosDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'novoPortfolio/projetos_confirm_delete.html'
    success_url = reverse_lazy('projetos_list')




def contato(request):
    return render(request, 'novoPortfolio/contato.html')

def index(request):
    return render(request, 'novoPortfolio/index.html')