from django.shortcuts import render,redirect
from shop.forms import UserSignupForm,AddtocartForm,UserUpdateForm
from django.http import HttpResponse
from shop.models import Product,Cart
from Onlineshop import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User

def home(request):
	return render(request,'shop/header.html')
def signUp(request):
	if request.method=='POST':
		form = UserSignupForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('<script>alert("User Data inserted successfully")</script>') and redirect('signIn')
	form = UserSignupForm()
	return render(request,'shop/signUp.html',{'form':form})





# Create your views here.
def LoginView(request):
	if request.method=='POST':
		form = UserSigninForm(request.POST)
		if form.is_valid():
			return redirect('main')
	form = UserSigninForm()
	return render(request,'shop/signUp.html',{'form':form})
#def signOut(request):
	#return redirect('main')
def main(request):
	data = Cart.objects.filter(user_id=request.user.id)
	count=0
	for val in data:
		count=count+1
	return render(request,'shop/header.html',{'count':count})
def usvwe(request):
	d = UsReg.objects.all()
	return render(request,'shop/electronics.html',{'r':d})
# def elevw(request):
# 	d = Product.objects.filter(category_id='1')
# 	return render(request,'shop/electronics.html',{'e':d})
# def elevw1(request):
# 	d = Product.objects.filter(category_id='1')
# 	data = Cart.objects.filter(user_id=request.user.id)
# 	count=0
# 	for val in data:
# 		count=count+1
# 	return render(request,'shop/electronics1.html',{'e':d,'count':count})
def cloth(request):
	d = Product.objects.filter(category_id='2')
	return render(request,'shop/clothing.html',{'c':d})
def cloth1(request):
	d = Product.objects.filter(category_id='2')
	data = Cart.objects.filter(user_id=request.user.id)
	count=0
	for val in data:
		count=count+1
	return render(request,'shop/clothing.html',{'c':d,'count':count})
def foot(request):
	d = Product.objects.filter(category_id='3')
	return render(request,'shop/footwear.html',{'f':d})
def foot1(request):
	d = Product.objects.filter(category_id='3')
	data = Cart.objects.filter(user_id=request.user.id)
	count=0
	for val in data:
		count=count+1
	return render(request,'shop/footwear.html',{'f':d,'count':count})
def kids(request):
	d = Product.objects.filter(category_id='4')
	return render(request,'shop/kids.html',{'k':d})
def kids1(request):
	d = Product.objects.filter(category_id='4')
	data = Cart.objects.filter(user_id=request.user.id)
	count=0
	for val in data:
		count=count+1
	return render(request,'shop/kids.html',{'k':d,'count':count})
def jew(request):
	d = Product.objects.filter(category_id='5')
	return render(request,'shop/jew.html',{'j':d})
def jew1(request):
	d = Product.objects.filter(category_id='5')
	data = Cart.objects.filter(user_id=request.user.id)
	count=0
	for val in data:
		count=count+1
	return render(request,'shop/jew.html',{'j':d,'count':count})
def sports(request):
	d = Product.objects.filter(category_id='6')
	return render(request,'shop/sports.html',{'s':d})
def sports1(request):
	d = Product.objects.filter(category_id='6')
	data = Cart.objects.filter(user_id=request.user.id)
	count=0
	for val in data:
		count=count+1
	return render(request,'shop/sports.html',{'s':d,'count':count})
# def dec(request):
# 	d = Product.objects.filter(category_id='7')
# 	return render(request,'shop/dec.html',{'d':d})
# def dec1(request):
# 	d = Product.objects.filter(category_id='7')
# 	data = Cart.objects.filter(user_id=request.user.id)
# 	count=0
# 	for val in data:
# 		count=count+1
# 	return render(request,'shop/dec1.html',{'d':d,'count':count})
# def clean(request):
# 	d = Product.objects.filter(category_id='8')
# 	return render(request,'shop/clean.html',{'c':d})
# def clean1(request):
# 	d = Product.objects.filter(category_id='8')
# 	data = Cart.objects.filter(user_id=request.user.id)
# 	count=0
# 	for val in data:
# 		count=count+1
# 	return render(request,'shop/clean1.html',{'c':d,'count':count})
# def books(request):
# 	d = Product.objects.filter(category_id='9')
# 	return render(request,'shop/books.html',{'b':d})
# def books1(request):
# 	d = Product.objects.filter(category_id='9')
# 	data = Cart.objects.filter(user_id=request.user.id)
# 	count=0
# 	for val in data:
# 		count=count+1
	#return render(request,'shop/books1.html',{'b':d,'count':count})
def la(request):
	d = Product.objects.filter(category_id='7')
	return render(request,'shop/la.html',{'la':d})
def la1(request):
	d = Product.objects.filter(category_id='7')
	data = Cart.objects.filter(user_id=request.user.id)
	count=0
	for val in data:
		count=count+1
	return render(request,'shop/la.html',{'la':d,'count':count})
def trends(request):
	d = Product.objects.filter(category_id='8')
	return render(request,'shop/trends.html',{'t':d})
def trends1(request):
	d = Product.objects.filter(category_id='8')
	data = Cart.objects.filter(user_id=request.user.id)
	count=0
	for val in data:
		count=count+1
	return render(request,'shop/trends.html',{'t':d,'count':count})
def bs(request):
	d = Product.objects.filter(category_id='9')
	return render(request,'shop/bs.html',{'bs':d})
def bs1(request):
	d = Product.objects.filter(category_id='9')
	data = Cart.objects.filter(user_id=request.user.id)
	count=0
	for val in data:
		count=count+1
	return render(request,'shop/bs.html',{'bs':d,'count':count})
def tb(request):
	d = Product.objects.filter(category_id='10')
	return render(request,'shop/tb.html',{'tb':d})
def tb1(request):
	d = Product.objects.filter(category_id='10')
	data = Cart.objects.filter(user_id=request.user.id)
	count=0
	for val in data:
		count=count+1
	return render(request,'shop/tb.html',{'tb':d,'count':count})

def msg(request):
	data = Cart.objects.filter(user_id=request.user.id)
	count=0
	for val in data:
		count=count+1
	return render(request,'shop/msg.html',{'count':count})
	
def addtocart(request,id):
	r=Product.objects.get(id=id)
	if request.method == 'POST':
		p=Cart(user_id=request.user.id,product_id=id)
		p.save()
		
		return redirect('main')
	
	return render(request,'shop/tb.html',{'data':r})
def mycart(request):
	data = Cart.objects.filter(user_id=request.user.id)
	sum=0
	count=0
	for val in data:
		sum=sum+val.product.price
		count=count+1
	return render(request,'shop/mycart.html',{'data':data,'total':sum,'count':count})
def remove(request,kl):
	t = Cart.objects.get(id=kl)
	t.delete()
	return HttpResponse("product Deleted succesfully") and redirect('mycart')
def purchase(request):
	data = Cart.objects.filter(user_id=request.user.id)
	rid=request.user.id
	sum=0
	count=0
	for val in data:
		sum=sum+val.product.price
		count=count+1
	return render(request,'shop/purchase.html',{'data':data,'count':count,'total':sum,'id':rid})
def checkout(request):
	data=Cart.objects.filter(user_id=request.user.id)
	
	m=request.user.email
	receiver=m
	l=[]
	sum=0
	for i in data:
		sum=sum+i.product.price
		l.append(i.product.name)
	message='Ordered items ::\n'+' ,'.join(l)+'\n'+ ' will be delivered within 15 days.\n'+'Total amount paid: Rs.'+str(sum)+'\n'+'THANK YOU for Shopping!!'
	subject='Order confirmed'
	
	sender=settings.EMAIL_HOST_USER
	send_mail(subject,message,sender,[receiver])
	
	data.delete()
	return redirect('msg')
def profile(request):
	mail=request.user.email
	firstname=request.user.first_name
	lastname=request.user.last_name
	i=request.user.id
	data = Cart.objects.filter(user_id=request.user.id)
	count=0
	for val in data:
		count=count+1
	return render(request,'shop/profile.html',{'mail':mail,'fn':firstname,'ln':lastname,'i':i,'count':count})
def search(request):
	try:
		q=request.GET.get('q')
	except:
		q=None
	if q:
		p1=Product.objects.filter(name__icontains=q)
		
		template="shop/search.html"
	data = Cart.objects.filter(user_id=request.user.id)
	count=0
	for val in data:
		count=count+1
	return render(request,template,{'query':q,'p1':p1,'count':count})
def search1(request):
	try:
		q=request.GET.get('q')
	except:
		q=None
	if q:
		p1=Product.objects.filter(name__icontains=q)
		context={'query':q,'p1':p1}
		template="shop/search1.html"
	return render(request,template,context)
def edit(request,pl):
	fg=User.objects.get(id=pl)
	if request.method == "POST":
		ft=UserUpdateForm(request.POST,request.FILES,instance=fg)
		if ft.is_valid():
			ft.save()
			return redirect("main")
	ft=UserUpdateForm(instance=fg)
	return render(request,'shop/edit.html',{'usg':ft})







