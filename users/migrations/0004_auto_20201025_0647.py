# Generated by Django 3.0.5 on 2020-10-25 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201021_1539'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['id']},
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='confirmation_code',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='bio',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='О себе'),
        ),
    ]