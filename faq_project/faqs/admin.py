from django.contrib import admin
from .models import FAQ
from ckeditor.widgets import CKEditorWidget
from django import forms

class FAQAdminForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = '__all__'
        widgets = {
            'answer': CKEditorWidget(),
        }

class FAQAdmin(admin.ModelAdmin):
    form = FAQAdminForm

admin.site.register(FAQ, FAQAdmin)
