# Generated by Django 3.1 on 2020-08-28 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'verbose_name': '职位', 'verbose_name_plural': '职位列表'},
        ),
    ]