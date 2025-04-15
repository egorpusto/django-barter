from django import forms
from .models import Ad, ExchangeProposal
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


# Form for creating and editing ads
class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'image_url', 'category', 'condition']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image_url': 'Image URL',
            'category': 'Category',
            'condition': 'Condition',
        }

    # Custom validation for title
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise ValidationError('Title must be at least 5 characters long.')
        return title

    # Custom validation for image_url
    def clean_image_url(self):
        image_url = self.cleaned_data.get('image_url')
        if image_url:
            validator = URLValidator()
            try:
                validator(image_url)
            except ValidationError:
                raise ValidationError('Invalid URL format.')
        return image_url

    # Custom validation for category
    def clean_category(self):
        category = self.cleaned_data.get('category')
        if len(category) < 3:
            raise ValidationError(
                'Category must be at least 3 characters long.')
        return category


# Form for creating exchange proposals
class ExchangeProposalForm(forms.ModelForm):
    class Meta:
        model = ExchangeProposal
        fields = ['ad_sender', 'ad_receiver', 'comment']
        labels = {
            'ad_sender': 'Your Ad',
            'ad_receiver': 'Receiver Ad',
            'comment': 'Comment',
        }

    # Custom validation for comment
    def clean_comment(self):
        comment = self.cleaned_data.get('comment')
        if len(comment) < 10:
            raise ValidationError(
                'Comment must be at least 10 characters long.')
        return comment
