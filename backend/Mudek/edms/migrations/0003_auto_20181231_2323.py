# Generated by Django 2.1.4 on 2018-12-31 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edms', '0002_auto_20181231_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='exam_type',
            field=models.CharField(max_length=50, verbose_name='Sınav Türü'),
        ),
    ]