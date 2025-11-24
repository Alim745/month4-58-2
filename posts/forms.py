from django import forms
from posts.models import Post


class PostForm(forms.Form):
    image = forms.ImageField(label="Image", required=False)
    title = forms.CharField(label="Title", max_length=200)
    content = forms.CharField(label="Content", max_length=1000)
    rate = forms.IntegerField(label="Rate", min_value=1, max_value=10)

    def clean_title(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if title.lower() == "javascript":
            raise forms.ValidationError("Javascript is a bad language")
        return title
    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            return image
        name = image.name.split('.')[-1]
        if name not in ['jpg', 'png', 'jpeg']:
            raise forms.ValidationError("Only .jpg, .png and .jpeg images are allowed")
        return image


class PostForm2(forms.ModelForm):
    class Meta:
       model = Post
       fields = ['image', 'title', 'content', 'rate']

    def clean_title(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if title.lower() == "javascript":
            raise forms.ValidationError("Javascript is a bad language")
        return title
    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            return image
        name = image.name.split('.')[-1]
        if name not in ['jpg', 'png', 'jpeg']:
            raise forms.ValidationError("Only .jpg, .png and .jpeg images are allowed")
        return image