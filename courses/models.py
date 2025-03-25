from django.db import models
from django.db.models import CASCADE

from users.models import CustomUser


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание',blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Course(models.Model):
    students = models.ManyToManyField(CustomUser,related_name='courses_enrolled',blank=True)
    #класс ForeignKey отвечает за связь текущей модели course и модели customuser ,тип связи 1 ко многим
    instructor = models.ForeignKey(CustomUser,on_delete=CASCADE,related_name='courses_created')
    title = models.CharField(max_length=100,verbose_name='название')
    description = models.TextField(verbose_name='описание')
    category = models.ForeignKey(Category,on_delete=CASCADE,related_name='category')
    ctreated = models.DateTimeField(auto_now_add=True,verbose_name='время создания')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'




class Lesson(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE, verbose_name='курс')
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    order = models.PositiveIntegerField(verbose_name='порядок уроков')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'











