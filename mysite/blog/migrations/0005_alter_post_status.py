# Generated by Django 4.1.7 on 2023-03-14 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_category_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[('publish', 'publish'), ('status', 'draft')], default=1),
        ),
    ]
