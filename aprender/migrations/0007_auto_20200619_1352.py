# Generated by Django 2.1.7 on 2020-06-19 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aprender', '0006_auto_20200614_2252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='quiz',
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ManyToManyField(related_name='questions', to='aprender.Quiz'),
        ),
    ]