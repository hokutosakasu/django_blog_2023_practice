# Generated by Django 4.0.5 on 2022-06-24 05:19

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=markdownx.models.MarkdownxField(verbose_name='本文'),
        ),
    ]
