from django import forms
from .models import Post,Cleanup,Response

class PolutionForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['message','photo','pollution_type','location','estimate']
    
class CleanupForm(forms.ModelForm):
    class Meta:
        model = Cleanup
        fields='__all__'
        
class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields=['reaction','estimate']
        
class CleanupForm(forms.ModelForm):
    class Meta:
        model = Cleanup
        fields=['location','organizer','organizer_contact','paybill','amount']