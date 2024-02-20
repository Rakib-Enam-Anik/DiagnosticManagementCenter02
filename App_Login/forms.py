from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import  AbstractUser
from django.db import transaction
from App_Login.models import DcmPatient, User, DcmDoctor


class SignUpForm(UserCreationForm):

    email = forms.EmailField( label="Email Address", required=True)
    
    class Meta:
        model = User
        fields = ('username',  'email', 'password1', 'password2')

class UserProfileChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

class ProfilePic(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_pic']
        

class DcmPatientSignUpForm(UserCreationForm):
    email=forms.EmailField(required=True)
  
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_dcmpatient = True
        user.save()
        patient = DcmPatient.objects.create(user=user)
        return user

class DcmDoctorSignUpForm(UserCreationForm):
    email=forms.EmailField(required=True)
    phone=forms.CharField(required=True)
    desination=forms.CharField(required=True)
  
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_ = True
        user.save()
        doctor = DcmDoctor.objects.create(user=user)
        doctor.phone=self.cleaned_data.get('phone')
        doctor.desination=self.cleaned_data.get('desination')
        doctor.save()

        return doctor

    
        
