# Generated by Django 2.2.16 on 2022-05-12 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220511_0526'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'user'), ('moderator', 'moderator'), ('admin', 'admin')], default='user', max_length=64),
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('email', 'username')},
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
    ]