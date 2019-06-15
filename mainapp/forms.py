from django import forms

from mainapp.models import Patient


class RegForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'middle_name', 'last_name', 'address1', 'address2', 'city', 'state',
                  'country', 'zip_code', 'dob', 'sex', 'phone_number', 'email', 'blood_group', 'remarks']
    # TODO datepicker
