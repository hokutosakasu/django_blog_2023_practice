# Generated by Django 4.0.5 on 2022-06-16 07:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200, verbose_name='カテゴリー')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='タイトル')),
                ('text', models.TextField(verbose_name='本文')),
                ('image', models.ImageField(upload_to='images/', verbose_name='画像')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日付')),
                ('updated_data', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category', verbose_name='カテゴリー')),
            ],
        ),
    ]
