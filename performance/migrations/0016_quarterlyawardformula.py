# Generated by Django 2.2 on 2020-03-02 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0015_quarterlyaward'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuarterlyAwardFormula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_item', models.CharField(max_length=100, verbose_name='指标')),
                ('formula', models.CharField(max_length=100, verbose_name='公式')),
            ],
            options={
                'verbose_name': '季度奖金公式表',
                'verbose_name_plural': '季度奖金公式表',
            },
        ),
    ]
