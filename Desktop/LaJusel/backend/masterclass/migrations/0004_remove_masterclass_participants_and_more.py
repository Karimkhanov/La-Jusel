# Generated by Django 4.1.7 on 2023-05-03 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterclass', '0003_alter_masterclass_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='masterclass',
            name='participants',
        ),
        migrations.AddField(
            model_name='masterclass',
            name='participants',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]