# Generated by Django 2.2 on 2020-03-10 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0022_systemconfig_backup_to_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemconfig',
            name='days_to_auto_backup',
            field=models.IntegerField(default=0, verbose_name='自动备份天数间隔'),
            preserve_default=False,
        ),
    ]