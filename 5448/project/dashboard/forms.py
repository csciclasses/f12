from django import forms

class AddActivityTypeForm(forms.Form):
    name = forms.CharField(max_length=50, label='Activity',
        widget=forms.TextInput(attrs={'placeholder': 'Activity Name'}),
        error_messages={
            'required': 'Activity name is required',
            'max_length': 'Activity name cannot be longer than 50 characters'
            })
