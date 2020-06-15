# Generated by Django 2.2.10 on 2020-06-14 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regiprofile',
            name='pet_age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='regiprofile',
            name='pet_gender',
            field=models.CharField(choices=[('남', '남'), ('여', '여'), ('중성', '중성')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='regiprofile',
            name='pet_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='regiprofile',
            name='pet_intro',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='regiprofile',
            name='pet_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='regiprofile',
            name='pet_type',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userlocation',
            name='ispermit',
            field=models.BooleanField(default=False, verbose_name=''),
        ),
    ]