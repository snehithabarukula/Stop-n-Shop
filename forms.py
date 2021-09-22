from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from shop.models import Cart

class UserSignupForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email']
class UserSigninForm(AuthenticationForm):
	class Meta:
		model=User
class UserUpdateForm(ModelForm):
	class Meta:
		model=User
		
		fields=['username','first_name','last_name','email']
		
		

class AddtocartForm(ModelForm):
	class Meta:
		model = Cart
		fields=['user','product']

		
		