from django.db import models

# Create your models here.
class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text

class Post(models.Model):
    header_image = models.ImageField()


class imggal(models.Model):
    imgtitle=models.CharField(max_length=100)
    imgdesc=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
        