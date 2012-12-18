from django import forms


class ReportForm(forms.Form):
    activity_type = forms.ChoiceField(label='Activity Type:',
        error_messages={
            'required': 'Activity Type is required',
            'invalid': 'Invalid Activity Type selected'},
            choices=[])
    from_date = forms.DateField(label='From:', required=False,
        error_messages={
        'invalid': 'Invalid From date'},
        widget=forms.TextInput(attrs={'placeholder':'mm/dd/yy'}))
    to_date = forms.DateField(label='To:', required=False,
        error_messages={
        'invalid': 'Invalid To date'},
        widget=forms.TextInput(attrs={'placeholder':'mm/dd/yy'}))

    def prepare(self, activity_type_list):
        choices = map(lambda x: (x['id'], x['name']), activity_type_list)
        choices = [('-1', ' - All Activity Type')] + choices
        self.fields['activity_type'].choices = choices
