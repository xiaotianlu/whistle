from User.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class CreationForm(UserCreationForm):
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'QQ',
                  'sex',
                  ]
        labels = { 'sex': '性别', }


