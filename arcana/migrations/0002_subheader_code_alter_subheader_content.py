# Generated by Django 5.1.6 on 2025-03-01 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arcana', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subheader',
            name='code',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='subheader',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
