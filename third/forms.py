from django.forms import ModelForm
from django import forms
from third.models import Restaurant, Review
from django.utils.translation import gettext_lazy as _

REVIEW_POINT_CHOICES = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
)


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['point', 'comment', 'restaurant']
        labels = {
            'point': _('펑점'),
            'comment': _('코멘트'),
        }
        help_texts = {
            'point': _('펑점을 입력해주세요.'),
            'comment': _('코멘트를 입력해주세요.'),
        }
        widgets = {
            'restaurant': forms.HiddenInput(),
            'point': forms.Select(choices=REVIEW_POINT_CHOICES),
        }


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'address']
        labels = {
            'name': _('이름'),
            'address': _('주소'),
        }
        help_texts = {
            'name': _('이름을 입력해주세요.'),
            'address': _('주소를 입력해주세요.'),
        }
        error_messages = {
            'name': {
                'max_length': _('이름이 너무 깁니다. 30자 이하로 해주세요.')
            }
        }
