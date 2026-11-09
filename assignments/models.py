from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=50, unique=True)
    teacher = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.title} ({self.code})"

class Assignment(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.PROTECT,
        related_name='assignments'
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.course.title}"
