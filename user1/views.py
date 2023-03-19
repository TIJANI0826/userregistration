from django.contrib import messages

from django.db.transaction import commit
from django.shortcuts import redirect, render
from .models import Package,Laundry,TicketNumber,Members
from django.views.generic import CreateView,View
# Create your views here.
# views.py file
from django.http import HttpResponse,HttpResponseRedirect, request
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import CreateNewList,OrderLaundryForm

# Create your views here.
def index(response):
	user = response.user
	ls = Package.objects.all()
	return render(response, "home.html", {
		"ls":ls,
		'user': user,
	})

@method_decorator(login_required, name='dispatch')
class Index(View):
	template_name = 'home.html'
	def get(self, request, *args, **kwargs):
		# orderedLaundry = Laundry.objects.get(id = kwargs['pk'])
		order = Laundry.objects.filter(user = request.user)
		if not order:
			"""
			Don't show the result if the user didn't attempted the quiz
			"""
			messages.info(self.request,"No Laundry Ordered")        
			# questions = self.form_class(initial=self.initial
		return render(request,'home.html', { 'order':order} )

def create(response):
	if response.method == "POST":
		form = CreateNewList(response.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = CreateNewList()
	return render(response, "create.html", {"form":form})
	
@method_decorator(login_required, name='dispatch')
class OrderLaundry(CreateView):
	model = Laundry
	form_class = OrderLaundryForm
	template_name = 'orderlaundry.html'
	
	def get_context_data(self, **kwargs):
		kwargs['user'] = self.request.user
		return super().get_context_data(**kwargs)


	def get_object(self):
		return self.request.user
	
	def form_valid(self, form):
		
		order = form.save(commit=False)
		order.user = self.request.user
		order.save()
		messages.success(self.request, 'Laundry ordered with success!')
		return redirect('/')