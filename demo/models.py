from django.db import models


# Create your models here.
class MainModel(models.Model):
    title = models.CharField('title', db_column='title', max_length=32, null=False, blank=False)
    subtitle = models.CharField('subtitle', db_column='subtitle', max_length=128, null=False, blank=False)

    class Meta:
        managed = True
        db_table = 'main'
        verbose_name = 'Main'
        verbose_name_plural = 'MainItems'

    def __str__(self):
        return self.title


class PersonModel(models.Model):
    name = models.CharField('name', db_column='name', max_length=32, null=False, blank=False)
    age = models.IntegerField('age', db_column='age', null=True, blank=True, default=0)

    class Meta:
        managed = True
        db_table = 'person'
        verbose_name = 'Person'
        verbose_name_plural = 'People'

    def __str__(self):
        return self.name


class BookModel(models.Model):
    name = models.CharField('name', db_column='name', max_length=64, null=False, blank=False)

    class Meta:
        managed = True
        db_table = 'book'
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.name


class Prop1(models.Model):
    key = models.CharField('key', db_column='key', max_length=32, null=False, blank=False)
    value = models.CharField('value', db_column='value', max_length=32, null=False, blank=False)

    class Meta:
        managed = True
        db_table = 'prop1'
        verbose_name = 'Prop1'
        verbose_name_plural = 'Prop1'

    def __str__(self):
        return self.key


class Prop2(models.Model):
    key = models.CharField('key', db_column='key', max_length=32, null=False, blank=False)
    value = models.CharField('value', db_column='value', max_length=32, null=False, blank=False)

    class Meta:
        managed = True
        db_table = 'prop2'
        verbose_name = 'Prop2'
        verbose_name_plural = 'Prop2'

    def __str__(self):
        return self.key


class Config(models.Model):
    key = models.CharField('key', db_column='key', max_length=32, null=False, blank=False)
    value = models.CharField('value', db_column='value', max_length=32, null=False, blank=False)

    class Meta:
        managed = True
        db_table = 'config'
        verbose_name = 'Config'
        verbose_name_plural = 'Configs'

    def __str__(self):
        return self.key
