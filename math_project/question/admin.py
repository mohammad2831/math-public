from django import forms
from django.contrib import admin
from .models import Question, Stage

class StageInlineForm(forms.ModelForm):
    class Meta:
        model = Stage
        fields = ['stage_number',  'option1', 'option2', 'option3', 'option4', 'correct_option']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            
            self.fields['question'].queryset = Question.objects.filter(id=self.instance.question.id)

class StageInline(admin.TabularInline):
    model = Stage
    form = StageInlineForm
    extra = 1  
class QuestionAdmin(admin.ModelAdmin):
    inlines = [StageInline]
    fields = ['title', 'option1', 'option2', 'option3', 'option4', 'correct_option']  

admin.site.register(Question, QuestionAdmin)
