from django import forms
from django.contrib import admin
from .models import Question, Stage
from .forms import StageAdminForms

class StageInlineForm(forms.ModelForm):
    class Meta:
        model = Stage
       
        fields = [
            'option1_title',  
            'option1_image',
            'option2_title',
            'option2_image',
            'option3_title',
            'option3_image',
            'option4_title',
            'option4_image',
            'correct_option'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['question'].queryset = Question.objects.filter(id=self.instance.question.id)

class StageInline(admin.StackedInline):
    model = Stage
    form = StageAdminForms
    extra = 1  

  
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(stage_number__gt=1)


class QuestionAdmin(admin.ModelAdmin):
    inlines = [StageInline]
    form = StageAdminForms

admin.site.register(Question, QuestionAdmin)
admin.site.register(Stage)
