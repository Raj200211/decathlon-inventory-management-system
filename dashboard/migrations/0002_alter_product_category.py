# Generated by Django 4.2.7 on 2023-11-13 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Sports', 'Sports'), ('Exercise', 'Exercise'), ('Food', 'Food')], max_length=20, null=True),
        ),
    ]
