# Generated by Django 4.1.7 on 2023-03-30 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_rename_profile_pic_profile_profile_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='article_snippet',
            field=models.CharField(max_length=1000),
        ),
    ]
