from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    recipe = models.CharField(max_length=100)
    image = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_item')
