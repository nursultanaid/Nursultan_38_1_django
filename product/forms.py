from django import forms
from product.models import Product, Review


class ProductForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        label='Название',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }
        ))
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }
        )
    )
    image = forms.ImageField(
        required=False,
        label='Изображение',
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if 'product' in name:
            raise forms.ValidationError('You can not use this word!')

    def clean(self):
        name = self.cleaned_data.get('name')
        title = self.cleaned_data.get('title')

        if name == title:
            raise forms.ValidationError('The name and title cannot be the same!')
        return self.cleaned_data

class ProductForm2(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите название'
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите описание'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'price': forms.NumberInput(),
            'category': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tags': forms.SelectMultiple(
               attrs={
                   'class': 'form-control'
               }
            )
        }
        labels = {
            'name': 'Название',
            'title': 'Описание',
            'image': 'Изображение',
            }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        widgets = {
            'text' : forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ваш отзыв'
                }
            )
        }
        labels = {
            'text': 'Отзыв'
        }