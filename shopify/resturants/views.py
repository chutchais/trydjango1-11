from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView
from django.db.models import Q
# Create your views here.

from .forms import RestaurantForm,RestaurantLocationCreateForm
from .models import RestaurantLocation


class RestaurantListView(LoginRequiredMixin,ListView):
	# template_name = 'restaurants/restaurants_list.html' # default name =restaurantlocation_list.html
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)
		# print(self.kwargs)
		# slug = self.kwargs.get("slug")
		# if slug:
		# 	queryset = RestaurantLocation.objects.filter(
		# 		Q(name__icontains=slug) |
		# 		Q(name__iexact=slug)
		# 		)
		# else:
		# 	queryset = RestaurantLocation.objects.all()
		# return queryset

class RestaurantDetailView(LoginRequiredMixin,DetailView):
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)

# @login_required()
class RestaurantCreateView(LoginRequiredMixin,CreateView):
	form_class = RestaurantLocationCreateForm
	# login_url = '/login/'  #overwrite from setting
	template_name = 'form.html'
	# success_url = '/restaurants/'

	def form_valid(self,form):
		instance = form.save(commit=False)
		instance.owner = self.request.user
		return super(RestaurantCreateView,self).form_valid(form)

	def get_context_data(self,*args,**kwargs):
		context = super(RestaurantCreateView,self).get_context_data(*args,**kwargs)
		context['title']='Add Retaurant'
		return context

class RestaurantUpdateView(LoginRequiredMixin,UpdateView):
	form_class = RestaurantLocationCreateForm
	# login_url = '/login/'  #overwrite from setting
	template_name = 'resturants/detail-update.html'
	# success_url = '/restaurants/'

	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)


	def get_context_data(self,*args,**kwargs):
		context = super(RestaurantUpdateView,self).get_context_data(*args,**kwargs)
		name = self.get_object().name
		context['title']= f'Update Restaurant {name}'
		return context

# @login_required()
# def restaurant_createview(request):
# 	# form = RestaurantForm(request.POST or None)
# 	form = RestaurantLocationCreateForm(request.POST or None)
# 	errors = None
# 	if form.is_valid():
# 		# obj = RestaurantLocation.objects.create(
# 		# 	name= form.cleaned_data.get('name'),
# 		# 	location = form.cleaned_data.get('location'),
# 		# 	category = form.cleaned_data.get('category')
# 		# 	)
# 		if request.user.is_authenticated():
# 			instance = form.save(commit=False)
# 			instance.owner = request.user
# 			instance.save()
# 			return HttpResponseRedirect('/restaurants/')
# 		else :
# 			return HttpResponseRedirect('/login/')

# 	if form.errors:
# 		errors = form.errors

# 	template_name ='resturants/form.html'
# 	context = {'form':form,'errors':errors}
# 	return render(request,template_name,context)



# def restaurant_listview(request):
# 	template_name ='restaurants/restaurants_list.html'
# 	queryset = RestaurantLocation.objects.all()
# 	context = {
# 		"object_list" : queryset
# 	}
# 	return render(request,template_name,context)


# def home(request):
# 	# return HttpResponse("Hello")
# 	return render(request,"home.html",{})


# def about(request):
# 	# return HttpResponse("Hello")
# 	return render(request,"about.html",{})

# class AboutUsView(View):
# 	def get(self,request,*args,**kwarg):
# 		print (kwarg)
# 		context={}
# 		return render(request,"about.html",context)

# class HomeView(TemplateView):
# 	template_name ='home.html'
# 	def get_context_data(self,*args,**kwargs):
# 		context = super(HomeView,self).get_context_data(*args,**kwargs)
# 		print (context)
# 		return context

# class AboutUsView(TemplateView):
# 	template_name ='about.html'