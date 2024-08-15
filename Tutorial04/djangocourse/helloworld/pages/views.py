from django.views.generic import TemplateView
from django.views import View #ok
from django.http import HttpResponseRedirect #ok
from django.urls import reverse #ok
from django.contrib import messages

from django import forms #ok
from django.shortcuts import render, redirect #ok

class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Your Name",
        })

        return context
    
# ACTIVIDAD 1 - Adición de toda esta clase.
class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Contact us - Online Store",
            "subtitle": "Contact us",
            "application_email": "laempresa@hotmail.com",
            "address": "Calle 22 # 33-44",
            "phone_number": "(312) 456-7890",
        })
        
        return context
    

    # ACTIVIDAD 2 - Adición de productos en la barra de navegación (ver base.html).
    # ACTIVIDAD 3 - Adición de price en el diccionario de cada producto.
class Product:
    products = [
        {"id":"1", "name":"TV", "description":"Best TV", "price": 1000}, 
        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price": 800},
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price": 99},
        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price": 100},
    ]


class ProductIndexView(View):
    template_name = 'products/index.html'
    
    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products
        
        return render(request, self.template_name, viewData)
    

class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        viewData = {}
        # ACTIVIDAD 4 - Adición del Try - Except.
        try:
            product = Product.products[int(id)-1]
            viewData["title"] = product["name"] + " - Online Store"
            viewData["subtitle"] = product["name"] + " - Product information"
            viewData["product"] = product
            return render(request, self.template_name, viewData)
        except(IndexError, ValueError):
            messages.error(request, "Product ID not found")
            return HttpResponseRedirect(reverse('home'))


class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)
    # ACTIVIDAD 7 - Precio debe ser mayor a cero.
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price


class ProductCreateView(View):
    template_name = 'products/create.html'
    created_successful_template_name = 'products/created_successful.html'

    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)

        if form.is_valid():
            # ACTIVIDAD 8 - Producto creado exitosamente.
            return render(request, self.created_successful_template_name, {'title': 'Product created'})
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)


'''
class ProductCreateView(View):
    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {
            "title": "Create product",
            "form": form
        }
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)
        
        if form.is_valid():
            # Process the form data (save to database, etc.)
            # Example: 
            # product = Product.objects.create(name=form.cleaned_data['name'], price=form.cleaned_data['price'])

            # Redirect to a valid URL pattern name, e.g., 'product_list'
            return redirect('index')  # Replace 'product_list' with your actual URL pattern name
        else:
            viewData = {
                "title": "Create product",
                "form": form
            }
            return render(request, self.template_name, viewData)

'''