from django.db import models
#from django.utils.translation import ugettext as _
from django.utils.translation import gettext_lazy as _

from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from django.core.files.storage import default_storage as storage  

from django.contrib.auth.models import User

# Create your models here.

# Сотрудник
class Employee(models.Model):
    login = models.CharField(_('login'), max_length=96)
    password = models.CharField(_('password'), max_length=96)
    name = models.CharField(_('name'), max_length=96)
    email = models.CharField(_('email'), max_length=96)
    admin = models.BooleanField(default=False)
    manager = models.BooleanField(default=False)
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'employee'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['login']),
            models.Index(fields=['password']),
            models.Index(fields=['name']),
        ]
        # Сортировка по умолчанию
        ordering = ['login']

# За¤вка
class Request(models.Model):
    dater = models.DateTimeField(_('dater'), auto_now_add=True)
    customer = models.CharField(_('customer'), max_length=128)
    address = models.CharField(_('address'), max_length=128)
    phone = models.CharField(_('phone'), max_length=64)
    problem = models.TextField(_('problem'))
    cost = models.DecimalField(_('cost'), max_digits=6, decimal_places=2, blank=True, null=True)
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'request'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['dater']),
        ]
        # Сортировка по умолчанию
        ordering = ['dater']

# Движение за¤вки
class Stage(models.Model):
    request = models.ForeignKey(Request, related_name='stage_request', on_delete=models.CASCADE)
    dates = models.DateTimeField(_('dates'), auto_now_add=True)
    details = models.TextField(_('details'))
    employee = models.ForeignKey(Employee, related_name='request_employee', on_delete=models.CASCADE)    
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'stage'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['dates']),
        ]
        # Сортировка по умолчанию
        ordering = ['dates']
