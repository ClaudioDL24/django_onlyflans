# Generated by Django 4.2.11 on 2024-04-25 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('static_pages', '0002_contactform'),
    ]

    operations = [
        migrations.AddField(
            model_name='flan',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='flan',
            name='receta',
            field=models.TextField(default=''),
        ),
    ]
