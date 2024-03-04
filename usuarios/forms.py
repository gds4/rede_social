from django import forms
from .models import user_profile



class ProfileForm(forms.ModelForm):

    class Meta:
        model = user_profile
        fields = ('profile_image','name', 'surname', 'nickname', 'gender', 'bio')

        widgets = {
            'bio': forms.Textarea(attrs={'class':'form-control'}),
            'profile_image': forms.FileInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'surname': forms.TextInput(attrs={'class':'form-control'}),
            'nickname': forms.TextInput(attrs={'class':'form-control'}),
            'gender': forms.Select(attrs={'class':'form-control'}),
            'bio': forms.Textarea(attrs={'class':'form-control'}),
        }

