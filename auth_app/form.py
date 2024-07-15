from django import forms
from .models import PostModel, comments, Tags


class PostModelForm(forms.ModelForm):
    # content = forms.CharField(widget=forms.Textarea(attrs={'row':4}))
    tags = forms.ModelMultipleChoiceField(
        queryset=Tags.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    class Meta:
        model =PostModel
        fields=('title','content','tags')



class CommentForm(forms.ModelForm):
    # user = forms.ModelChoiceField(
    #     queryset=User.objects.all(),
    #     widget=forms.HiddenInput(),
    # )

    class Meta:
        model = comments
        # fields = ['user', 'text']
        fields = ['text']

class TagForm(forms.ModelForm):
    class Meta:
        model =Tags
        fields =['tags']