# Generated by Django 4.0.6 on 2022-08-17 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0005_commentmodel_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='FirstApp.tag'),
        ),
    ]
