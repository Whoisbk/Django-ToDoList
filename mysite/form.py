from django import forms

class RegisterUser(forms.Form):
    username = forms.CharField(max_length=200,label="Enter Username")
    fname = forms.CharField(max_length=200,label="Enter first name")
    lname = forms.CharField(max_length=200,label="Enter last name")
    email = forms.CharField(max_length=200,label="Enter Email")
    pass1 = forms.CharField(max_length=200,label="Enter Password")
    pass2 = forms.CharField(max_length=200,label="Re-type Password")

class SigninUser(forms.Form):
    username = forms.CharField(max_length=200,label="Enter Username")
    pass1 = forms.CharField(max_length=200,label="Enter Password")

class CreateToDoList(forms.Form):
    text = forms.CharField(max_length=200,label="Enter Task")