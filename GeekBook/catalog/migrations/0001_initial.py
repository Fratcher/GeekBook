# Generated by Django 5.0.6 on 2024-06-15 07:11

import django.db.models.deletion
import django.db.models.functions.text
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Died')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(help_text='Enter valid year format (e.g. 1999, 2021, etc.)', max_length=4, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=400)),
                ('summary', models.TextField(help_text='What is the story behind this one?? :)', max_length=1000)),
                ('isbn', models.CharField(help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13, unique=True, verbose_name='ISBN')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.author')),
            ],
        ),
        migrations.AddConstraint(
            model_name='year',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='year_name_case_insensitive_unique', violation_error_message='Year already exists (case insensitive match)'),
        ),
        migrations.AddField(
            model_name='description',
            name='year',
            field=models.ManyToManyField(help_text='Select a Year for this entry', to='catalog.year'),
        ),
    ]