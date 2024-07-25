from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Country(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class City(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Region(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Neighborhood(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class Question(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('text', 'Text'),
        ('image', 'Image'),
        ('video', 'Video'),
    ]
    title = models.CharField(max_length=255)
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPE_CHOICES)
    text_content = models.TextField(null=True, blank=True)
    image_content = models.URLField(null=True, blank=True)
    video_content = models.URLField(null=True, blank=True)
    answers = models.ManyToManyField("Answer", related_name='questions')
    balls = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('text', 'Text'),
        ('image', 'Image'),
    ]
    title = models.CharField(max_length=255)
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPE_CHOICES)
    text_content = models.TextField(null=True, blank=True)
    image_content = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title


class Test(models.Model):
    title = models.CharField(max_length=255)
    questions = models.ManyToManyField(Question, related_name='tests')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    balls = models.IntegerField()

    def __str__(self):
        return self.title
