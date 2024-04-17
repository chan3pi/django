from django.shortcuts import render 
from django.shortcuts import redirect
from django.contrib import messages 
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,SignUpForm,AddBookForm
from django.contrib.auth.forms import UserCreationForm
from .models import Book
from .forms import AddBookForm
# Create your views here.
def index(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data 
			user = authenticate(request,username = cd['username'],password = cd['password'])
			if user is not None:
				login(request,user)
				messages.success(request,"login successfully")
				return redirect('about')
			else:
				messages.success(request,'please try again')
				return redirect('index')
	else: 
		form=LoginForm()
	return render(request,'index.html',{'form':form})


def about(request):
	books = Book.objects.all()
	return render(request,"about.html",{'books':books})

def register(request):
	#register a new user
	if request.method=='post':
		#displaying registration form
		form=SignUpForm()
	else:
		#process completed form
		form=SignUpForm(data=request.POST)
	if form.is_valid():
		new_user=form.save()
		login(request,new_user)
		return redirect('index')
	#display a blank or invalid
	context={'form':form}
	return render(request,'register.html',context)

def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('/')


def add_book(request):
	form = AddBookForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == 'POST':
			if form.is_valid():
				add_book = form.save()
				messages.success(request,"book created successfully")
				return redirect('about')
		return render(request,'add.html',{'form':form})
	else:
		messages.success(request,"you must be logged in...")
		return redirect('index')

def book(request,pk):
    if request.user.is_authenticated:
        book_record = Book.objects.get(id=pk)
        return render(request,'book.html',{'book_record':book_record})
    else:
        return redirect('about')        
    
    
def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Book.objects.get(id=pk)
		form = AddBookForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "book Has Been Updated!")
			return redirect('about')
		return render(request, 'update.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('index')


def delete(request,pk):
    if request.user.is_authenticated:
        delete_it = Book.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"book deleted")
        return redirect('about')  
    else:
        messages.success(request,"you must be logged in")   
        return redirect('index') 