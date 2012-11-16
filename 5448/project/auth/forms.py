from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(max_length= 50, label='Email',
        widget=forms.TextInput(attrs={'placeholder':'Email address'}),
        error_messages={
            'required': 'Email is required',
            'invalid': 'Please enter a valid Email',
            'max_length': 'Email address cannot be longer than 50 characters'
            })

    password = forms.CharField(max_length=50, label='Password',
        widget=forms.TextInput(attrs={'placeholder':'Password'}),
        error_messages={
            'required': 'Password is required',
            'invalid': 'Please enter a valid Password',
            'max_length': 'Password cannot be longer than 50 characters'
            })