# Generated by Django 5.0.6 on 2024-09-13 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0008_alter_question_option1_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_option',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
