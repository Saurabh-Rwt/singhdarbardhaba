# Generated by Django 5.0 on 2024-01-15 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singhdarbarapp', '0008_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='static/assets/img/product'),
        ),
    ]
