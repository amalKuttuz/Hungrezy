# Generated by Django 4.1.1 on 2023-06-05 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_alter_categories_title_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(default='product_default.png', upload_to='product_image/'),
        ),
    ]
