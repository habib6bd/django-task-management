
from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(max_length= 250)
    description = forms.CharField(
        widget= forms.Textarea, label='Task Description'
    )
    due_date = forms.DateField(widget=forms.SelectDateWidget, label='Due Date')
    assign_to = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[], label='Assigned To')
    
    def __init__(self, *args, **kwargs):
        # print(args, kwargs)
        employees = kwargs.pop("employees", [])
        print(employees)
        super().__init__(*args, **kwargs)
        self.fields['assign_to'].choices = [
            (emp.id, emp.name) for emp in employees
        ]