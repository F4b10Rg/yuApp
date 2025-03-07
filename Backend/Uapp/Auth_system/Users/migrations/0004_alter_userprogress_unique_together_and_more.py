# Generated by Django 5.1.5 on 2025-02-13 03:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lessons', '0002_remove_lesson_lesson_type_lesson_description_and_more'),
        ('Users', '0003_remove_userprogress_chapter'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userprogress',
            unique_together={('user', 'lesson')},
        ),
        migrations.AddField(
            model_name='userprogress',
            name='progress',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='userprogress',
            name='lesson',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='progress', to='Lessons.lesson'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprogress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='userprogress',
            name='completion_date',
        ),
    ]
