# Generated by Django 5.0.7 on 2024-10-02 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_about_about_bulletpoint_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appconf',
            name='adress',
            field=models.CharField(default='test', max_length=50),
        ),
    ]
