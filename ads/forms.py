from django import forms
from .models import Ad, ExchangeProposal


# Форма для создания и редактирования объявлений
class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'image_url', 'category', 'condition']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'image_url': 'Ссылка на изображение',
            'category': 'Категория',
            'condition': 'Состояние',
        }


# Форма для создания предложений обмена
class ExchangeProposalForm(forms.ModelForm):
    class Meta:
        model = ExchangeProposal
        fields = ['ad_sender', 'ad_receiver', 'comment']
        labels = {
            'ad_sender': 'Ваше объявление',
            'ad_receiver': 'Объявление другого пользователя',
            'comment': 'Комментарий к предложению',
        }
