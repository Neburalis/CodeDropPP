import uuid
import os
from django.db import models


# Create your models here.


class CodeDropDB(models.Model):
    name = models.CharField(max_length=100)
    unique_id = models.CharField(max_length=10, unique=True, blank=True, null=True)
    # prog_lang = models.CharField(max_length=100, null=True, blank=True)
    # date_created = models.DateTimeField(auto_now_add=True)
    # date_removal = models.DateTimeField(null=True, blank=True)
    text = models.TextField()

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = self.generate_unique_id()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f'{self.id}'

    def __str__(self):
        return self.name

    def generate_unique_id(self):
        # hasher = hashlib.md5()
        # hasher.update(str(self.id).encode('utf-8'))
        # return hasher.hexdigest()[:10]

        # unique_id = uuid.uuid4().hex[:8]

        max_attempts = int(os.getenv('GENERATE_UNIQUE_ID_MAX_ATTEMPTS'))
        digits = int(os.getenv('GENERATE_UNIQUE_ID_DIGITS_COUNT'))
        for attempt in range(max_attempts):
            for _ in range(max_attempts):
                # while CodeDropDB.objects.filter(unique_id=unique_id).exists():
                unique_id = uuid.uuid4().hex[:digits+attempt]
                if not CodeDropDB.objects.filter(unique_id=unique_id).exists():
                    return unique_id
        raise Exception(f'Could not generate unique id for {self.name}')
