# Generated by Django 2.1.7 on 2019-06-11 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='exam_answer_file',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Cevap Anahtarı Dosya'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='exam_file',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Sınav Kağıdı Dosya'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_content_file',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Ders İçeriği Dosya'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_notes_file',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Ders Notu Dosya'),
        ),
    ]
