from django.db import models

# Create your models here.

class Member(models.Model):
    login_id=models.EmailField()
    apikey=models.TextField()
    auth_type=models.TextField()
    name=models.TextField()
    password=models.TextField()
    password_answer=models.TextField()
    password_question=models.TextField()

    def __str__(self) -> str:
        return super().__str__()