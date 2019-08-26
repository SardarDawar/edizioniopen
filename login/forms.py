from django import forms

class signupinfo(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    username = forms.CharField(max_length=25)
    email = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput())
    re_enter_password = forms.CharField(widget=forms.PasswordInput())
    paypal_url = forms.URLField()

class logininfo(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput())

class resetpassword(forms.Form):
    username = forms.CharField(max_length=25)
    new_password = forms.CharField(widget=forms.PasswordInput())

class forgotpassword1(forms.Form):
    username = forms.CharField(max_length=25)

class forgotpassword2(forms.Form):
    key_from_email = forms.CharField(max_length=10)
    new_password = forms.CharField(widget=forms.PasswordInput())