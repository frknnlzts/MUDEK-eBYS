# Generated by Django 2.1.7 on 2019-03-20 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff')),
                ('is_verified', models.BooleanField(default=False, verbose_name='Verified')),
                ('is_academician', models.BooleanField(default=True, verbose_name='Academician')),
                ('is_department_manager', models.BooleanField(default=False, verbose_name='Department Manager')),
                ('is_assistant_department_manager', models.BooleanField(default=False, verbose_name='Assistant Department Manager')),
                ('is_dean_manager', models.BooleanField(default=False, verbose_name='Dean Manager')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='ActivationKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=50, unique=True, verbose_name='Key')),
                ('is_used', models.BooleanField(default=False, verbose_name='Used')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activation_keys', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Activation Key',
                'verbose_name_plural': 'Activation Keys',
            },
        ),
        migrations.CreateModel(
            name='ResetPasswordKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=50, unique=True, verbose_name='Key')),
                ('is_used', models.BooleanField(default=False, verbose_name='Used')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reset_password_keys', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Reset Password Key',
                'verbose_name_plural': 'Reset Password Keys',
            },
        ),
    ]