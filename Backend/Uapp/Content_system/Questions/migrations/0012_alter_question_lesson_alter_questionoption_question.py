# Generated by Django 5.1.5 on 2025-02-22 01:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lessons', '0005_remove_lesson_questions_amount'),
        ('Questions', '0011_questiontype_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lessons.lesson'),
        ),
        migrations.AlterField(
            model_name='questionoption',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Questions.question'),
        ),
    ]
