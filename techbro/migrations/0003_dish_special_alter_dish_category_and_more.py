# Generated by Django 4.0.6 on 2022-08-11 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('techbro', '0002_alter_dish_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='special',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='dish',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='techbro.category'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='dish',
            name='image',
            field=models.ImageField(blank=True, default='pin.png', null=True, upload_to='food'),
        ),
    ]