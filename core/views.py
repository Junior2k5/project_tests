#from django.shortcuts import render

# Create your views here.
#from django.views.generic import TemplateView
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Servico, Funcionario, Recurso, Cliente, Preco
from .forms import ContatoForm

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['recursos_esquerda'] = Recurso.objects.order_by('recurso').all()[:3]
        context['recursos_direita'] = Recurso.objects.order_by('recurso').all()[3:6]
        context['clientes'] = Cliente.objects.order_by('?').all()
        context['precos'] = Preco.objects.order_by('mensalidade').all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
