from django.db import models

# Create your models here.
# db로 넘겨주기 (helloworld라는 모델을 만들어서 넘겨줌)
class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)