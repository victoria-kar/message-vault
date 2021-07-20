from django import forms


class MessageForm(forms.Form):
    username = forms.CharField(
        required=False,
        max_length=120,
        label="Name (Optional)",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Anonymous"}
        ),
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 4}),
    )
