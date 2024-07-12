from django import forms
from .models import PostModel, comments


class PostModelForm(forms.ModelForm):
    # content = forms.CharField(widget=forms.Textarea(attrs={'row':4}))

    class Meta:
        model =PostModel
        fields=('title','content')



class CommentForm(forms.ModelForm):
    # user = forms.ModelChoiceField(
    #     queryset=User.objects.all(),
    #     widget=forms.HiddenInput(),
    # )

    class Meta:
        model = comments
        # fields = ['user', 'text']
        fields = ['text']