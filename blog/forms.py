from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Book  
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


class SignUpForm(UserCreationForm):
      email = forms.EmailField(label="email",widget=forms.TextInput(attrs={'class':'form-control'}))
      first_name = forms.CharField(label="first_name",widget=forms.TextInput(attrs={'class':'form-control'}))
      last_name = forms.CharField(label="last_name",widget=forms.TextInput(attrs={'class':'form-control'}))


      class Meta:
           model = User
           fields = ('username','first_name','last_name','email','password1','password2')

      def __init__(self, *args, **kwargs):
           super(SignUpForm,self).__init__(*args, **kwargs)

    

           self.fields['username'].widget.attrs['class']='form-control'
           self.fields['username'].help_text='<span class="form-text text-muted"><strong>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. Password</strong></span>'
           self.fields['password1'].widget.attrs['class']='form-control'
           self.fields['password1'].help_text = '<ul class="form-text text-muted"><li>Your password can’t be too similar to your other personal information</li><li>Your password must contain at least 8 characters</li><li>Your password can’t be a commonly used password</li><li>Your password can’t be entirely numeric</li></ul>'
           self.fields['password2'].widget.attrs['class']='form-control'
           self.fields['password2'].help_text='<span class="form-text text-muted"><strong>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. Password</strong></span>'


class AddBookForm(forms.ModelForm):
      title = forms.CharField(label="title",widget=forms.TextInput(attrs={'class':'form-control'}))
      author = forms.CharField(label="author",widget=forms.TextInput(attrs={'class':'form-control'}))
      body = forms.CharField(label="body",widget=forms.Textarea(attrs={'class':'form-control'}))

      class Meta:
          model = Book
          exclude = ("User",) 