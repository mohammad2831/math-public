from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=255)  
    option1 = models.CharField(max_length=255,default="")
    option2 = models.CharField(max_length=255,default="")
    option3 = models.CharField(max_length=255,default="")
    option4 = models.CharField(max_length=255,default="")
    correct_option = models.CharField(max_length=255, default=1)  

    def __str__(self):
        return self.title

class Stage(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='stages')
    stage_number = models.PositiveIntegerField()  
    option1 = models.CharField(max_length=255,default="") 
    option2 = models.CharField(max_length=255,default="")  
    option3 = models.CharField(max_length=255,default="")  
    option4 = models.CharField(max_length=255,default="")  
    correct_option = models.CharField(max_length=255, default=1)  

    def __str__(self):
        return f"Stage {self.stage_number} for {self.question.title}"
