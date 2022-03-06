from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields= ["title", "content","image" ]
        widgets = {
            
            'title': forms.TextInput( attrs={'class': 'form-control','style':'width:100%'}),
            'content': forms.Textarea( attrs={'class': 'form-control','style':'width:100%',}),
            'image': forms.FileInput( attrs={'class': 'form-control','style':'width:100%',}),
            

            
        }
        labels={
            'title':'Blog Title',
            'content': 'Body',

        }
