from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm
from django.views import generic
from django.urls import reverse_lazy



def index(request):
    product_list = Product.objects.all()
    context = {'product_list':product_list}
    return render(request,'mobileApp/index.html',context)

class IndexView(generic.ListView):
    model = Product
    template_name = 'mobileApp/index.html'
    context_object_name = 'product_list'


def detail(request,prod_id):
    product = Product.objects.get(pk=prod_id)
    context = {'product':product}
    return render(request,'mobileApp/detail.html',context)


class DetailView(generic.DeleteView):
    model = Product
    template_name = 'mobileApp/detail.html'

def create_product(request):
    form  = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mobileApp:index')
    
    return render(request,'mobileApp/create.html',{'form':form})

class CreateProduct(generic.edit.CreateView):
    model = Product
    fields = '__all__'
    template_name = 'mobileApp/create.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)
    
def update_product(request,id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('mobileApp:index')
    context = {'form':form,'product':product}
    return render(request,'mobileApp/create.html',context)

class UpdateProduct(generic.edit.UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'mobileApp/create.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

class DeleteProduct(generic.DeleteView):
    model = Product
    slug_field = 'pk'
    

def delete_product(request,id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        product.delete()
        return redirect('mobileApp:index')
    return render(request,'mobileApp/delete.html',{'product':product})
    

class DeleteProduct(generic.DeleteView):
    model = Product
    success_url = reverse_lazy('mobileApp:index')
    template_name = 'mobileApp/delete.html'



