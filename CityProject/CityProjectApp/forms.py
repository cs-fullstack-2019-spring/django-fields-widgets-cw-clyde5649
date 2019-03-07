from django import forms
from .models import CityApplication


RICH_OR_POWERS=(
    ('RICH'),
    ('SUPERPOWERS')

)

SUPERPOWERS=(
    ('FLIGHT'),
    ('SPEED')
)


city_of_orgin=(
    ('MEMPHIS TN'),
    ('JACKSON TN'),

)


class CityApplicationform(forms.ModelForm):
    class Meta:
        model = CityApplication
        fields = '__all__'
        widgets = {
            'date': forms.SelectDateWidget()



            }