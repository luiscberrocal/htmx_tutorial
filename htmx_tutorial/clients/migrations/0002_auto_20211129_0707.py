# Generated by Django 3.2.9 on 2021-11-29 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is active'),
        ),
        migrations.AddField(
            model_name='client',
            name='sex',
            field=models.CharField(default='U', max_length=1, verbose_name='Sex'),
        ),
    ]
