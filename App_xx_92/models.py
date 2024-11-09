from django.db import models

class Study(models.Model):
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Hobby(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
