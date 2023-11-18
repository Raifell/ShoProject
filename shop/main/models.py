from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    name = models.CharField('Name', max_length=255)
    description = models.TextField('Description', null=True)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, verbose_name='Category')
    photo = models.ImageField('Photo', upload_to='product/%Y/%m/%d', null=True, blank=True)
    price = models.PositiveIntegerField('Price')
    count = models.PositiveIntegerField('Count')
    date = models.DateField('Date', auto_now_add=True)
    slug = models.SlugField('Slug', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify('{}-{}'.format(self.name, self.category))
        super(Product, self).save(force_insert, force_update, using, update_fields)


class Category(models.Model):
    name = models.CharField('Name', max_length=255)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user_name = models.CharField('Name', max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField('Comment')
    date = models.DateField('Date', auto_now_add=True)

    def __str__(self):
        return self.user_name
