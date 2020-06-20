# Generated by Django 2.1.7 on 2020-06-11 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aprender', '0002_auto_20200611_0005'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='choice',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='slug',
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='aprender.Quiz'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
