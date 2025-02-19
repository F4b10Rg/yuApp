# Generated by Django 5.1.5 on 2025-02-19 05:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lessons', '0004_remove_lesson_score_lesson_questions_amount'),
        ('Tags', '0001_initial'),
        ('WordPhrases', '0003_remove_wordphrase_tags_wordphrase_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordphrase',
            name='tags',
            field=models.ManyToManyField(related_name='word_phrases', to='Tags.tag'),
        ),
        migrations.AddField(
            model_name='wordphrase',
            name='type',
            field=models.CharField(choices=[('word', 'Word'), ('phrase', 'Phrase')], default=('word', 'Word'), max_length=10),
        ),
        migrations.AlterField(
            model_name='wordphrase',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lessons.lesson'),
        ),
    ]
