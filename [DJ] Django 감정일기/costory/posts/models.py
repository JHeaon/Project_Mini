from django.db import models

# Create your models here.
class Post(models.Model):
    # models.Model 을 상속하여 사용한다.
    title = models.CharField(max_length=50)
    # CharField는 길이 제한이 있는 구조
    content = models.TextField()
    # TextField는 길이 제한 없는 구조 
    dt_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    dt_modified = models.DateTimeField(verbose_name="Dtate Modified", auto_now=True)
    # 날짜와 시간을 함께 다루는 필드
    
    def __str__(self) -> str:
        return self.title