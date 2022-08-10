# Generated by Django 2.2.16 on 2022-05-21 10:39

import reviews.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0010_auto_20220521_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='rating',
            field=models.PositiveIntegerField(default=1, validators=[reviews.validators.validate_score]),
            preserve_default=False,
        ),
    ]