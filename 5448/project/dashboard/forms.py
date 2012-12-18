from django import forms


class AddActivityTypeForm(forms.Form):
    name = forms.CharField(max_length=50, label='Activity Type',
        widget=forms.TextInput(attrs={'placeholder': 'Activity Type'}),
        error_messages={
            'required': 'Activity Type is required',
            'max_length': 'Activity Type cannot be longer than 50 characters'})


class CreateActivityForm(forms.Form):
    activity_type = forms.ChoiceField(label='Activity Type',
        error_messages={
            'required': 'Activity Type is required',
            'invalid': 'Invalid Activity Type selected'},
            choices=[])
    hours = forms.IntegerField(required=False, label='Hours', min_value=0, max_value=23,
        error_messages={
            'invalid': 'Incorrect value entered for hours',
            'min_value': 'Hours cannot be less than 0',
            'max_value': 'Hours cannot be greater than 23'}, initial=0)
    minutes = forms.IntegerField(required=False, label='Minutes', min_value=0, max_value=59,
        error_messages={
            'invalid': 'Incorrect value entered for minutes',
            'min_value': 'Minutes cannot be less than 0',
            'max_value': 'Minutes cannot be greater than 59'}, initial=0)
    seconds = forms.IntegerField(required=False, label='Seconds', min_value=0, max_value=59,
        error_messages={
            'invalid': 'Incorrect value entered for seconds',
            'min_value': 'Seconds cannot be less than 0',
            'max_value': 'Seconds cannot be greater than 59'}, initial=0)

    def prepare(self, activity_type_list):
        choices = map(lambda x: (x['id'], x['name']), activity_type_list)
        self.fields['activity_type'].choices = choices
