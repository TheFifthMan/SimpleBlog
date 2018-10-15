from django import forms
from .models import Comment

class CommentModelForm(forms.Form):
    username = forms.CharField(required=True,
                                widget=forms.TextInput(
                                    attrs={
                                        'id':"id_name",
                                        "name":"name",
                                        }))
    email = forms.CharField(required=True,
                            widget=forms.TextInput(
                                attrs={
                                    "id":"id_email",
                                    "name":"email",
                                }))
    url = forms.CharField(required=True,
                        widget=forms.TextInput(
                            attrs={
                                "id":"id_url",
                                "name":"url",
                            }))
                            
    body = forms.CharField(required=True,
                    widget=forms.Textarea(
                        attrs={
                            "id":"id_comment",
                            "name":"comment",
                        }))
