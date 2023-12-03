from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignupForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', )
        
        
    def save(self):
        user = super().save()
      
        return user