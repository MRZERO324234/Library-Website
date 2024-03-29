# Generated by Django 4.2.7 on 2024-01-29 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0025_auto_20220222_0623'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.SlugField(default=1, max_length=250, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=0, max_length=250, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='books', to='catalog.author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Select a genre for this book', related_name='books', to='catalog.genre'),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(help_text='13 Character ISBN number', max_length=13, unique=True, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(help_text='Enter a book genre (e.g. Science Fiction, French Poetry etc.)', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)", max_length=200, unique=True),
        ),
    ]
