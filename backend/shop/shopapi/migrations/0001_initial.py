# Generated by Django 4.2.5 on 2023-10-22 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(max_length=32)),
                ('product_name', models.CharField(max_length=64)),
                ('product_description', models.CharField(max_length=1024)),
                ('product_price', models.FloatField()),
                ('product_img_url', models.CharField(max_length=512)),
            ],
        ),
    ]
