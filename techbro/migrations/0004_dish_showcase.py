# Generated by Django 4.0.6 on 2022-08-11 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techbro', '0003_dish_special_alter_dish_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='showcase',
            field=models.BooleanField(default=False),
        ),
    ]
