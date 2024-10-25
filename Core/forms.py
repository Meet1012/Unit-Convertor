# your_app/forms.py
from django import forms

LENGTH_UNIT_CHOICES = [
    ('meters', 'Meters'),
    ('kilometers', 'Kilometers'),
    ('centimeters', 'Centimeters'),
    ('millimeters', 'Millimeters'),
    ('inches', 'Inches'),
    ('feet', 'Feet'),
    ('yards', 'Yards'),
    ('miles', 'Miles')
]

WEIGHT_UNIT_CHOICES = [
    ('grams', 'Grams'),
    ('kilograms', 'Kilograms'),
    ('pounds', 'Pounds'),
    ('ounces', 'Ounces'),
    ('stones', 'Stones')
]

TEMPERATURE_UNIT_CHOICES = [
    ('celsius', 'Celsius'),
    ('fahrenheit', 'Fahrenheit'),
    ('kelvin', 'Kelvin')
]

class LengthConverter(forms.Form):
    length = forms.DecimalField(label="Length to Convert", max_digits=10, decimal_places=2)
    unit_from = forms.ChoiceField(label="Convert From", choices=LENGTH_UNIT_CHOICES)
    unit_to = forms.ChoiceField(label="Convert To", choices=LENGTH_UNIT_CHOICES)
        
class WeightConverter(forms.Form):
    weight = forms.DecimalField(label="Weight to Convert", max_digits=10, decimal_places=2)
    unit_from = forms.ChoiceField(label="Convert From", choices=WEIGHT_UNIT_CHOICES)
    unit_to = forms.ChoiceField(label="Convert To", choices=WEIGHT_UNIT_CHOICES)
    
class TemperatureConverter(forms.Form):
    temp = forms.DecimalField(label="Temperature to Convert", max_digits=10, decimal_places=2)
    unit_from = forms.ChoiceField(label="Convert From", choices=TEMPERATURE_UNIT_CHOICES)
    unit_to = forms.ChoiceField(label="Convert To", choices=TEMPERATURE_UNIT_CHOICES)
