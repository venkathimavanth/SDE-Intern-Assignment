# Generated by Django 2.1 on 2019-11-22 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrymodel',
            name='host',
        ),
        migrations.RemoveField(
            model_name='exitmodel',
            name='host',
        ),
        migrations.DeleteModel(
            name='EntryModel',
        ),
        migrations.DeleteModel(
            name='ExitModel',
        ),
        migrations.DeleteModel(
            name='Host',
        ),
    ]