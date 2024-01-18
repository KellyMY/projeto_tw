from django.db import models
from django import forms
# from user.models.user import User as userdata

class User(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    email = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

class UserRegister(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_repeat = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "password", "email", "image"
                  )
        
    # def samePassword(self):
    #     cd = self.cleaned_data

    #     username = userdata.objects.filter(cd["username"])

    #     if cd["password"] != cd["password_repeat"]:
    #         raise forms.ValidationError("Senha não são iguais!")
    #     elif username is not None:
    #         raise forms.ValidationError("Nome de usuário já existe!")
    #     return cd["password_repeat"]
    

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user_following = models.ManyToManyField(User, blank=True)