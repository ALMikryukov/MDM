import json
from django.db import models

# Create your models here.
#
# class Person(models.Model):
#     name = models.CharField(max_length=20)
#     age = models.IntegerField()
#     DoesNotExist = models.Manager
# #  связь по  ключу
# class Company(models.Model):
#     name = models.CharField(max_length=30)
#
# class Product (models.Model):
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     name = models.CharField(max_length=30)
#     price = models.IntegerField()
# #     many to many
# class Course(models.Model):
#     name= models.CharField(max_length=20)
#
# class Student(models.Model):
#     name = models.CharField(max_length=30)
#     courses = models.ManyToManyField(Course)
# # one to one
# class User(models.Model):
#     name =  models.CharField(max_length=20)
#
# class Account (models.Model):
#     login = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class PartItem(models.Model):
    brand = models.ForeignKey('PartBrand', on_delete=models.CASCADE,null=True )
    oem = models.CharField(max_length=25)
    name  =  models.CharField(max_length=150)
    # img =  models.ImageField(blank=True, upload_to='Parts')
    cond = models.ForeignKey('Conditions', blank=True, on_delete=models.SET_NULL, null=True)
    quantaty = models.IntegerField(null=True)
    app = models.ManyToManyField('CarModels', blank=True)
    analogs = models.ManyToManyField('PartItem', blank=True)
    category = models.ForeignKey('Catalog', on_delete=models.SET_NULL, null=True)
    price  =  models.IntegerField(blank=True, null=True)
    oemIn = models.CharField(max_length=25, blank=True)
    featured_image = models.ImageField(null=True, blank=True,default='default.jpg',upload_to='Parts')

    def toJSON(self):
        return json.dumps(self, default=vars,
            sort_keys=True, indent=4)

    def __str__(self):
        return str(self.oem +   ' '  + self.name )
    class Meta:
        verbose_name ='Склад'
        verbose_name_plural = 'Склад'




class PartBrand(models.Model):
    name = models.CharField(max_length=250, null=True, unique=True)
    # img = models.ImageField(blank=True, )
    history = models.TextField(blank=True, max_length=500)
    featured_image = models.ImageField(null=True, blank=True,default='default.jpg',upload_to='PartBrands')
    country =  models.ForeignKey('Contryes',on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.name+ ' '+ str(self.country))
    class Meta:
        verbose_name ='Производитель'
        verbose_name_plural = 'Производители'


class Contryes(models.Model):
    name = models.CharField(max_length=30, null=True, unique=True)
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Страна Производителя'
        verbose_name_plural = 'Страны Производителей'

class Conditions(models.Model):
    name =  models.CharField(max_length=150)
    logo = models.ImageField(blank=True, upload_to='Condition_logo')
    desc  =   models.TextField(max_length=900, blank=True)

    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = 'Состояние товара'
        verbose_name_plural = 'Состояния товара'


class CarBrands(models.Model):
    name = models.CharField(max_length=30, unique=True, null=True)
    logo = models.ImageField(blank=True, upload_to='CarBrands')
    history = models.CharField(max_length=500, blank=True)
    models = models.ManyToManyField('CarModels', blank=True)

    def __str__(self):
        return str(self.name)


    class Meta:
        ordering = ['name']
        verbose_name ='Марки авто'
        verbose_name_plural = 'Марки авто'


class CarModels(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=True, null=True)
    # logo = models.ImageField( blank=True)
    brand = models.ForeignKey(CarBrands, on_delete=models.CASCADE,blank=True)
    featured_image = models.ImageField(null=True, blank=True,default='default.jpg', upload_to='CarModels')


    def __str__(self):
        return str(str(self.brand)+' '+self.name)

    class Meta:
        verbose_name = 'Модели авто'
        verbose_name_plural= 'Модели авто'

class Catalog(models.Model):
    category = models.CharField(max_length=35)
    logo = models.ImageField(blank=True, upload_to='Category_logo')
    desc = models.CharField(max_length=35, blank=True)

    def __str__(self):
        return str(self.category)

    class Meta:

        verbose_name ='Категория товаров'
        verbose_name_plural = 'Категории товаров'




