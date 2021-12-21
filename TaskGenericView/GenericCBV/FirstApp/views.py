from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from .models import Laptop

class AddView(CreateView):
    model = Laptop
    fields = '__all__'
    success_url = '/pro/show/'

class ShowView(ListView):
    model = Laptop

class Delete(DeleteView):
    model = Laptop
    success_url = '/pro/show/'

class Update(UpdateView):
    model = Laptop
    fields = '__all__'
    success_url = '/pro/show/'



