from django.db import models

class DownloadFile(models.Model):
    CATEGORY_CHOICES = [
        ('video', 'Video'),
        ('audio', 'Audio'),
        ('pdf', 'PDF'),
        ('app', 'App'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    file = models.FileField(upload_to='downloads/')
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)

    views = models.PositiveIntegerField(default=0)
    downloads = models.PositiveIntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
