# Generated by Django 5.0.6 on 2024-09-13 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0006_remove_question_option1_test_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='option1_image_basa64',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stage',
            name='option2_image_basa64',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stage',
            name='option3_image_basa64',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stage',
            name='option4_image_basa64',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stage',
            name='option1_image',
            field=models.ImageField(default=1, upload_to=''),
        ),
        migrations.AlterField(
            model_name='stage',
            name='option2_image',
            field=models.ImageField(default=1, upload_to=''),
        ),
        migrations.AlterField(
            model_name='stage',
            name='option3_image',
            field=models.ImageField(default=1, upload_to=''),
        ),
        migrations.AlterField(
            model_name='stage',
            name='option4_image',
            field=models.ImageField(default=1, upload_to=''),
        ),
    ]