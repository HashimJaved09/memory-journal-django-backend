from django.contrib import admin
from django import forms


from accounts.models import User


class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class Account(admin.ModelAdmin):
    form = UserAdminForm

    def save_model(self, request, obj, form, change):
        if obj.pk:
            orig_obj = User.objects.get(pk=obj.pk)
            if obj.password != orig_obj.password:
                obj.set_password(obj.password)
        else:
            obj.set_password(obj.password)
        obj.save()


admin.site.register(User, Account)