from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    text = models.TextField('Текст',max_length=250 )
   
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'TITLE'
        verbose_name_plural = 'TEXT'
