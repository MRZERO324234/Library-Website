# Generated by Django 4.2.7 on 2024-01-30 11:56

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0027_alter_author_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=1, editable=False, populate_from='full_name', unique=True),
            preserve_default=False,
        ),
    ]
