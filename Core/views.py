# your_app/views.py
from decimal import Decimal, ROUND_HALF_UP
from decimal import Decimal
from django.shortcuts import render
from .forms import LengthConverter, WeightConverter, TemperatureConverter


def convert(request):
    length_form = LengthConverter()
    weight_form = WeightConverter()
    temp_form = TemperatureConverter()
    length_value = weight_value = temp_value = None
    if request.method == 'POST':
        if 'convert_length' in request.POST:
            length_form = LengthConverter(request.POST)
            if length_form.is_valid():
                length = length_form.cleaned_data['length']
                unit_from = length_form.cleaned_data['unit_from']
                unit_to = length_form.cleaned_data['unit_to']
                length_value = conversion(length, unit_from, unit_to)
        elif 'convert_weight' in request.POST:
            weight_form = WeightConverter(request.POST)
            if weight_form.is_valid():
                weight = weight_form.cleaned_data['weight']
                unit_from = weight_form.cleaned_data['unit_from']
                unit_to = weight_form.cleaned_data['unit_to']
                weight_value = conversion(weight, unit_from, unit_to)
        elif 'convert_temperature' in request.POST:
            temp_form = TemperatureConverter(request.POST)
            if temp_form.is_valid():
                temperature = temp_form.cleaned_data['temp']
                unit_from = temp_form.cleaned_data['unit_from']
                unit_to = temp_form.cleaned_data['unit_to']
                temp_value = conversion(temperature, unit_from, unit_to)
                
    active_tab = request.GET.get('tab', 'length')

    return render(request, 'temp.html', {
        'length_form': length_form,
        'weight_form': weight_form,
        'temp_form': temp_form,
        'length_value': length_value,
        'weight_value': weight_value,
        'temp_value': temp_value,
        'active_tab': active_tab
    })

# Example utility function


def conversion(value, unit_from, unit_to):
    # Ensure value is a Decimal instance
    value = Decimal(value)

    # Conversion factors for length (from unit_from to meters, using Decimal)
    length_factors = {
        "meters": Decimal('1'),
        "kilometers": Decimal('1000'),
        "centimeters": Decimal('0.01'),
        "millimeters": Decimal('0.001'),
        "inches": Decimal('0.0254'),
        "feet": Decimal('0.3048'),
        "yards": Decimal('0.9144'),
        "miles": Decimal('1609.34')
    }

    # Conversion factors for weight (from unit_from to grams, using Decimal)
    weight_factors = {
        "grams": Decimal('1'),
        "kilograms": Decimal('1000'),
        "pounds": Decimal('453.592'),
        "ounces": Decimal('28.3495'),
        "stones": Decimal('6350.29')
    }

    # Conversion functions for temperature using Decimal for precision
    def convert_temperature(temp, from_unit, to_unit):
        if from_unit == to_unit:
            return temp
        elif from_unit == "celsius":
            if to_unit == "fahrenheit":
                return (temp * Decimal('9')/Decimal('5')) + Decimal('32')
            elif to_unit == "kelvin":
                return temp + Decimal('273.15')
        elif from_unit == "fahrenheit":
            if to_unit == "celsius":
                return (temp - Decimal('32')) * Decimal('5')/Decimal('9')
            elif to_unit == "kelvin":
                return (temp - Decimal('32')) * Decimal('5')/Decimal('9') + Decimal('273.15')
        elif from_unit == "kelvin":
            if to_unit == "celsius":
                return temp - Decimal('273.15')
            elif to_unit == "fahrenheit":
                return (temp - Decimal('273.15')) * Decimal('9')/Decimal('5') + Decimal('32')
        return None

    # Rounding to 2 decimal places function
    def round_to_2_decimals(val):
        return val.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    # Length conversion
    if unit_from in length_factors and unit_to in length_factors:
        value_in_meters = value * \
            length_factors[unit_from]  # Convert to meters
        converted_value = value_in_meters / \
            length_factors[unit_to]  # Convert to target unit
        return round_to_2_decimals(converted_value)

    # Weight conversion
    elif unit_from in weight_factors and unit_to in weight_factors:
        value_in_grams = value * weight_factors[unit_from]  # Convert to grams
        converted_value = value_in_grams / \
            weight_factors[unit_to]  # Convert to target unit
        return round_to_2_decimals(converted_value)

    # Temperature conversion
    elif unit_from in ["celsius", "fahrenheit", "kelvin"] and unit_to in ["celsius", "fahrenheit", "kelvin"]:
        converted_value = convert_temperature(value, unit_from, unit_to)
        return round_to_2_decimals(converted_value)

    # If no conversion is possible, return None
    return None
