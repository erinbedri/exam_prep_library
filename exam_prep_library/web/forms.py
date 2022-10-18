from django import forms

from exam_prep_library.web.models import Book, Profile


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description'}),
            'image': forms.URLInput(attrs={'placeholder': 'Image'}),
            'type': forms.TextInput(attrs={'placeholder': 'Type'}),
        }


class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'readonly': True}),
            'last_name': forms.TextInput(attrs={'readonly': True}),
            'image_url': forms.URLInput(attrs={'readonly': True}),
        }
