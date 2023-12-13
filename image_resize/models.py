from django.db import models
from PIL import Image
import os
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime


class FoodPhoto(models.Model):
    TYPE_CHOICES = (
        ('kolacja', 'Kolacja'),
        ('obiad', 'Obiad'),
        ('sniadanie', 'Śniadanie'),
    )

    DIGEST_CHOICES = (
        ('latwo', 'Łatwostrawna'),
        ('podst', 'Podstawowa'),
    )

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/%Y/%m/')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='obiad')
    digest = models.CharField(max_length=20, choices=DIGEST_CHOICES, default='latwo')

    def generate_name(self):
        type = self.type
        digest = self.digest
        current_date = datetime.now().strftime('%d-%m-%y')
        return f"{type}{digest}{current_date}"

    def save(self, *args, **kwargs):
        self.name = self.generate_name()
        super().save(*args, **kwargs)

    @property
    def filename(self):
        return f"{self.name}{os.path.splitext(self.image.name)[1]}"


@receiver(post_save, sender=FoodPhoto)
def resize_and_rename_image(sender, instance, **kwargs):
    filepath = instance.image.path
    img = Image.open(filepath)
    img.thumbnail((1008, 756))

    new_filename = instance.filename
    new_filepath = os.path.join(os.path.dirname(filepath), new_filename)

    img.save(new_filepath)
    img.close()

    if os.path.exists(filepath):
        os.remove(filepath)


class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')