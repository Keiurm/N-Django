from django import forms


class TutorialForm(forms.Form):
    height = forms.FloatField(label="height")
    weight = forms.FloatField(label="weight")
