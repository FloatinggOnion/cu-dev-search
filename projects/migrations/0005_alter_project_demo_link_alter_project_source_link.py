# Generated by Django 4.1 on 2022-08-29 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_updated_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='demo_link',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='source_link',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]
