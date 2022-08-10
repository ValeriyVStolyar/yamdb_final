# Generated by Django 2.2.16 on 2022-05-21 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20220521_1258'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='user',
            name='unique_email_username',
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('email', 'username')},
        ),
    ]