# Generated by Django 2.2.10 on 2020-06-15 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200615_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plusphoto',
            name='plus_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
