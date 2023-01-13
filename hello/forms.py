from django import forms

class UserForm(forms.Form):
    name = forms.CharField(
        label="name",initial="undefined",
        help_text="Please, input your name.",
        required=True,min_length=2, max_length=20)
    age = forms.IntegerField(label="Age",initial=18, required=True)
    comment = forms.CharField(label="Comment", widget=forms.Textarea(attrs={"class":"myfield"}))
    mina = forms.ChoiceField(label="Language",choices=((1, "English"), (2, "German"), (3, "French")))
    password = forms.CharField(widget=forms.widgets.PasswordInput())
    field_order = ["name", "age", "mina"]
    required_css_class = "field"
    error_css_class = "error"
    special_css_class = "body"
    block_css_class = "block"