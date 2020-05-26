from django import forms

class AddCommentForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea)
