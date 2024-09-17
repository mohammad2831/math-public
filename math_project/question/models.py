from django.db import models
from accounts.models import User

class Question(models.Model):
    title = models.CharField(max_length=255)  

    option1_title = models.CharField(max_length=255,default="")
    option1_image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    option1_image_basa64 = models.TextField(blank=True, null=True)

    option2_title = models.CharField(max_length=255,default="")
    option2_image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    option2_image_basa64 = models.TextField(blank=True, null=True)

    option3_title = models.CharField(max_length=255,default="")
    option3_image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    option3_image_basa64 = models.TextField(blank=True, null=True)

    option4_title = models.CharField(max_length=255,default="")
    option4_image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    option4_image_basa64 = models.TextField(blank=True, null=True)

    correct_option = models.PositiveSmallIntegerField(default=1)  


    def __str__(self):
        return f"{self.id} - {self.title}"
    
       
    def save(self, *args, **kwargs):
      
        super().save(*args, **kwargs)
        
     
        if not Stage.objects.filter(question=self, stage_number=1).exists():
          
            Stage.objects.create(
                question=self,
                stage_number=1,
                option1_title=self.option1_title,
                option1_image=self.option1_image,
                option1_image_basa64=self.option1_image_basa64,
                option2_title=self.option2_title,
                option2_image=self.option2_image,
                option2_image_basa64=self.option2_image_basa64,
                option3_title=self.option3_title,
                option3_image=self.option3_image,
                option3_image_basa64=self.option3_image_basa64,
                option4_title=self.option4_title,
                option4_image=self.option4_image,
                option4_image_basa64=self.option4_image_basa64,
                correct_option=self.correct_option,
            )



class Stage(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='stages')
    stage_number = models.PositiveIntegerField()  
        
    option1_title = models.CharField(max_length=255,default="")
    option1_image = models.ImageField(default=1)
    option1_image_basa64 = models.TextField(blank=True, null=True)

    option2_title = models.CharField(max_length=255,default="")
    option2_image = models.ImageField(default=1)
    option2_image_basa64 = models.TextField(blank=True, null=True)

    option3_title = models.CharField(max_length=255,default="")
    option3_image = models.ImageField(default=1)
    option3_image_basa64 = models.TextField(blank=True, null=True)

    option4_title = models.CharField(max_length=255,default="")
    option4_image = models.ImageField(default=1)
    option4_image_basa64 = models.TextField(blank=True, null=True)

    correct_option = models.CharField(max_length=255, default=1)  

    def __str__(self):
        return f"Stage {self.stage_number} for {self.question.title}"



class UserScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question')
    score = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user} - {self.question} - {self.score}'
