# Generated by Django 2.1.7 on 2019-06-16 20:53

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import edms.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_type', models.CharField(blank=True, max_length=50, null=True, verbose_name='Sınav Türü')),
                ('exam_information', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True, verbose_name='Sınav Hakkında Bilgi')),
                ('exam_file', models.FileField(blank=True, null=True, upload_to=edms.models.other_directory_path, validators=[edms.models.validate_file_extension], verbose_name='Sınav Kağıdı Dosya')),
                ('exam_answer_file', models.FileField(blank=True, null=True, upload_to=edms.models.other_directory_path, validators=[edms.models.validate_file_extension], verbose_name='Cevap Anahtarı Dosya')),
            ],
            options={
                'verbose_name': 'Exam',
                'verbose_name_plural': 'Exam',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name', models.CharField(max_length=150, verbose_name='Ders Adı')),
                ('lesson_content', ckeditor.fields.RichTextField(blank=True, verbose_name='Ders İçeriği')),
                ('lesson_content_file', models.FileField(blank=True, null=True, upload_to=edms.models.lesson_directory_path, validators=[edms.models.validate_file_extension], verbose_name='Ders İçeriği Dosya')),
                ('lesson_notes', ckeditor.fields.RichTextField(blank=True, verbose_name='Ders Notu')),
                ('lesson_notes_file', models.FileField(blank=True, null=True, upload_to=edms.models.lesson_directory_path, validators=[edms.models.validate_file_extension], verbose_name='Ders Notu Dosya')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Lesson',
                'verbose_name_plural': 'Lesson',
            },
        ),
        migrations.CreateModel(
            name='Other_Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(blank=True, null=True, upload_to=edms.models.other_directory_path, validators=[edms.models.validate_file_extension], verbose_name='Dosya')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edms.Lesson')),
            ],
            options={
                'verbose_name': 'Other Document',
                'verbose_name_plural': 'Other Document',
            },
        ),
        migrations.CreateModel(
            name='Requested_Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_name', models.CharField(max_length=100, verbose_name='İstenilen Belge Adı')),
                ('d_bool', models.BooleanField(default=False, verbose_name='İstenilen Belge Yüklü mü ?')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edms.Lesson')),
            ],
            options={
                'verbose_name': 'Requested Documents',
                'verbose_name_plural': 'Requested Documents',
            },
        ),
        migrations.AddField(
            model_name='other_document',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edms.Requested_Documents'),
        ),
        migrations.AddField(
            model_name='exam',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edms.Lesson'),
        ),
    ]
