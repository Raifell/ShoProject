# Generated by Django 4.2.7 on 2023-11-18 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='product/%Y/%m/%d', verbose_name='Photo')),
                ('price', models.PositiveIntegerField(verbose_name='Price')),
                ('count', models.PositiveIntegerField(verbose_name='Count')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date')),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.category', verbose_name='Category')),
            ],
        ),
    ]
