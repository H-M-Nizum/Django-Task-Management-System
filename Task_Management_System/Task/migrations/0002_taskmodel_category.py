# Generated by Django 4.2.7 on 2023-12-07 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0002_remove_categorymodel_tasks'),
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='category',
            field=models.ManyToManyField(to='Category.categorymodel'),
        ),
    ]
