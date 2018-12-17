from .forms import habitForm
from .models import Habit
from django.shortcuts import render,redirect
from django.views.generic import TemplateView


class HomeView(TemplateView):
	template_name = 'power/home.html'

 
	def get(self, request):
		form = habitForm()
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form = habitForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/edit')

class EditView(TemplateView):
	template_name = 'power/edit.html'

	def get(self,request):
		habits = Habit.objects.all()
		return render(request,self.template_name,{'habits':habits})

