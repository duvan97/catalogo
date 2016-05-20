# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from catalogo.apps.ventas.forms import add_product_form
from catalogo.apps.ventas.forms import marca_form
from catalogo.apps.ventas.forms import categoria_form
from catalogo.apps.ventas.models import Producto
from catalogo.apps.ventas.models import Marca
from catalogo.apps.ventas.models import Categoria
from django.http import HttpResponseRedirect

def add_producto_view(request):
	info = "inicializando"
	if request.method == "POST":
		formulario = add_product_form(request.POST, request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.status = True
			add.save()
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect('/producto/%s' %add.id)
	else:
		formulario = add_product_form()
	ctx = {'form':formulario, 'informacion':info}
	return render_to_response('ventas/add_producto.html', ctx, context_instance = RequestContext(request))
def marca_view(request):
	info = "inicializando"
	if request.method == "POST":
		formulario = marca_form(request.POST)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.save()	
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect('/marca/%s' %add.id)
	else:
		formulario = marca_form()
	ctx = {'form':formulario, 'informacion':info}
	return render_to_response('ventas/marca.html', ctx, context_instance = RequestContext(request))
def categoria_view(request):
	info = "inicializando"
	if request.method == "POST":
		formulario = categoria_form(request.POST)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.save()	
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect('/categoria/%s' %add.id)
	else:
		formulario = categoria_form()
	ctx = {'form':formulario, 'informacion':info}
	return render_to_response('ventas/categoria.html', ctx, context_instance = RequestContext(request))

def edit_product_view(request, id_prod):
	info= ""
	prod = Producto.objects.get(pk = id_prod)
	if request.method =="POST":
		formulario = add_product_form(request.POST, request.FILES, instance = prod)
		if formulario.is_valid():
			edit_prod = formulario.save(commit = False)
			formulario.save_m2m()
			edit_prod.status = True
			edit_prod.save()
			info = "Guardadop Satisfactoriamente"
			return HttpResponseRedirect('/producto/%s'% edit_prod.id)
	else:
		formulario = add_product_form(instance = prod)
	ctx = {'form':formulario, 'informacion':info}
	return render_to_response('home/edit_producto.html', ctx, context_instance = RequestContext(request))

def del_product_view(request, id_prod):
	info = "inicializando"
	try:
		prod = Producto.objects.get(pk = id_prod)
		prod.delete()
		info = "Producto Eliminado Correctamente"
		return HttpResponseRedirect('/productos/')
	except:
		info = "Producto no se puede eliminar"

		return HttpResponseRedirect('/productos/')
