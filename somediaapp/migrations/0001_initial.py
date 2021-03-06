# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-12 01:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=32)),
                ('tweet', models.TextField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='TweetReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=10, max_digits=64)),
                ('longitude', models.DecimalField(decimal_places=10, max_digits=64)),
                ('status', models.CharField(max_length=3)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='somediaapp.Product')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=64, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='somediaapp.UserProfile'),
        ),
    ]
