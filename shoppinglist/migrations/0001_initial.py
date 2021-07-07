# Generated by Django 3.2.5 on 2021-07-07 02:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名前')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='新規登録日時')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名前')),
                ('price', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='金額')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='新規登録日時')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='個数')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='新規登録日時')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名前')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='新規登録日時')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
        ),
    ]