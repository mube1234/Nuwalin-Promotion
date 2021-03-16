from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class SignUpForm(UserCreationForm):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']
        widgets={
              'frist_name': forms.TextInput(attrs={'class': 'form-control',}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',}),
            'username':forms.TextInput(),
            'email':forms.TextInput(),
            'password1':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}),
        }
        help_texts = {
            'password1': "* Your password must contain at least 8 characters.",
            'password2': "* Your password can’t be entirely numeric.",
        }
    def save(self, commit=True):
        user=super(SignUpForm,self).save(commit=False)
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        if commit:
            user.save()
        return user

class AddNewsForm(forms.ModelForm):
    class Meta:
        model = Add_News
        fields = [ 'author','title','type','body','image']
        widgets = {
            'author': forms.TextInput(attrs={'type': 'hidden'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', }),
            'last_name': forms.TextInput(attrs={'class': 'form-control', }),
            'username': forms.TextInput(attrs={'class': 'form-control', }),
            'email': forms.TextInput(attrs={'class': 'form-control', }),

        }
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['address','work','gender','phone','image']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control', }),
            'work': forms.TextInput(attrs={'class': 'form-control', }),
            'phone': forms.TextInput(attrs={'class': 'form-control', }),
            'gender': forms.Select(attrs={'class': 'form-control', }),

        }
class SalesPromotionForm(forms.ModelForm):
    class Meta:
        model=SalesPromotion
        fields='__all__'
        widgets = {
            'owner': forms.TextInput(attrs={'type': 'hidden'}),
            'status': forms.TextInput(attrs={'type': 'hidden'}),
            'date_posted': forms.TextInput(attrs={'type': 'hidden'}),
        }

        help_texts = {
            'contact_info': "* Phone number you want to be contacted",
            'address': "* your business hosting address ",
            'specific_area': "* your business hosting specific area (sefer) ",
            'image3': "optional if you want",
        }
class AdvertisingForm(forms.ModelForm):
    class Meta:
        model=Adertising
        fields='__all__'
        widgets = {
            'ad_owner': forms.TextInput(attrs={'type': 'hidden'}),
            'status': forms.TextInput(attrs={'type': 'hidden'}),
            'date_posted': forms.TextInput(attrs={'type': 'hidden'})
        }

        help_texts = {
            'contact_info': "* Phone number you want to be contacted",
            'address': "* your business hosting address ",
            'specific_area': "* your business hosting specific area (sefer) ",
            'image3': "optional if you want",
        }

class OtherPromotionForm(forms.ModelForm):
    class Meta:
        model=OtherPromotion
        fields='__all__'
        widgets = {
            'owner': forms.TextInput(attrs={'type': 'hidden'}),
             'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'type': 'hidden'}),
            'date_posted': forms.TextInput(attrs={'type': 'hidden'})
        }

        help_texts = {
            'phone': "* Phone number you want to be contacted",
            'description': "* put detail idea of your promotion here",
        }
class AttachPromotionForm(forms.ModelForm):
    class Meta:
        model=AttachPromotion
        fields='__all__'
        widgets = {
            'author': forms.TextInput(attrs={'type': 'hidden'}),
            'date_posted': forms.TextInput(attrs={'type': 'hidden'}),
            'likes': forms.TextInput(attrs={'type': 'hidden'})
        }
class EditAttachPromotionForm(forms.ModelForm):
    class Meta:
        model=AttachPromotion
        fields = ['business_name','address','specific_area','description','image1','image2','image3','contact_info']
class EditNewsForm(forms.ModelForm):
    class Meta:
        model=Add_News
        fields=['type','title','body','image']

class PromotionCategoryForm(forms.ModelForm):
    class Meta:
        model=PromotionCategory
        fields=['name']
class SuggestForm(forms.ModelForm):
    class Meta:
        model=Suggestion
        fields=['user','suggestion']
        widgets = {
              'user':forms.TextInput(attrs={'type':'hidden'}),
             'suggestion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'your suggestion here!',})
        }
class FqaForm(forms.ModelForm):
    class Meta:
        model=Fqa
        fields='__all__'
        widgets = {
              'user':forms.TextInput(attrs={'type':'hidden'}),
              'question': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'your question here!',})
        }
class MoneyStartForm(forms.ModelForm):
    class Meta:
        model=MoneyQuestion
        fields='__all__'
        widgets = {
              'user':forms.TextInput(attrs={'readonly':'readonly'}),
              }

        help_texts = {
            'user': "* Your identification",
            'place': "* Your current address",
            'check': "* Are you ready to work with us? (yes/no) ",

        }
class SalesPromotionConfirmForm(forms.ModelForm):
    class Meta:
        model=SalesPromotion
        fields=['status']
class AdvertisementConfirmForm(forms.ModelForm):
    class Meta:
        model=Adertising
        fields=['status']

class OtherPromotionConfirmForm(forms.ModelForm):
    class Meta:
        model=OtherPromotion
        fields=['status']