from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=50, label='Email',
        widget=forms.TextInput(attrs={'placeholder': 'Email address'}),
        error_messages={
            'required': 'Email is required',
            'invalid': 'Please enter a valid Email',
            'max_length': 'Email address cannot be longer than 50 characters'
            })

    password = forms.CharField(max_length=50, label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        error_messages={
            'required': 'Password is required',
            'invalid': 'Please enter a valid Password',
            'max_length': 'Password cannot be longer than 50 characters'
            })


class NewUserForm(LoginForm):
    confirm_password = forms.CharField(max_length=50, label='Confirm Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        error_messages={
            'required': 'Confirm Password is required',
            'invalid': 'Please enter a valid Confirm Password',
            'max_length': 'Confirm Password cannot be longer than 50 characters'
            })

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()

        if cleaned_data and 'confirm_password' in cleaned_data and 'password' in cleaned_data and cleaned_data['confirm_password'] != cleaned_data['password']:
            raise forms.ValidationError('Password values do not match.')
        else:
            return cleaned_data
