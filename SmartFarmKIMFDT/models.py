from django.conf import settings
from django.db import models
from django.utils import timezone
from hashlib import md5

"""
Category of plants that are created by users
"""
class Vegetable(models.Model):
    type_name = models.CharField(max_length=200)
    duration = models.IntegerField()
    create_record_timestamp = models.DateTimeField(default=timezone.now)
    description = models.TextField()

    def __str__(self):
        return self.type_name

"""
Vegetables that are being planted in the farm
"""
class Plant(models.Model):
    plant_type = models.CharField(max_length=200)
    keep_total = models.IntegerField()
    keep_unit = models.CharField(max_length=30)
    sensor = models.CharField(max_length=200)
    start_plant_timestamp = models.DateTimeField()
    end_plant_timestamp = models.DateTimeField()
    create_record_timestamp = models.DateTimeField(default=timezone.now)
    is_harvested = models.BooleanField()

    def __str__(self):
        return "{}_{}".format(self._type_name, self._create_record_timestamp)

"""
Category of plants that are created by users
"""
class Compost(models.Model):
    plant_id = models.IntegerField()
    compost_type = models.CharField(max_length=30)
    compost_total = models.IntegerField()
    compost_unit = models.CharField(max_length=30)
    compost_date = models.DateTimeField(default=timezone.now)
    create_record_timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.compost_type

class User(models.Model):
    username = models.CharField(max_length=30)
    raw_password = models.CharField(max_length=30)
    digest_pass = models.CharField(max_length=30)
    last_send_pwd_time = models.DateTimeField(default=timezone.now)
    email = models.CharField(max_length=50)

    # _get_md5 = lambda self, x: md5.new(x).hexdigest()
    def _get_md5(self, x):
        m = md5()
        m.update(bytes(x, encoding="utf-8"))
        return m.digest()

    def _change_password(self, old_pass, new_pass):
        if self.digest_pass == self._get_md5(old_pass) or self.digest_pass == "":
            self.raw_password = new_pass
            self.digest_pass = self._get_md5(new_pass)
            self.save()
            return True
        return False

    def _change_email(self, pwd, email):
        if self.digest_pass == self._get_md5(pwd) or self.digest_pass == "":
            self.email = email
            self.save()
            return True
        return False

    def _validate_password(self, password):
        if self.digest_pass == self._get_md5(password) or self.digest_pass == "":
            return True
        return False