# Generated by Django 4.0.4 on 2022-06-04 12:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('movies', '0005_genrefilmwork_film_work_genre_idx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmwork',
            name='creation_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='creation_date'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='file_path',
            field=models.FileField(blank=True, null=True, upload_to='movies/', verbose_name='file_path'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='rating',
            field=models.FloatField(blank=True, default=0,
                                    validators=[django.core.validators.MinValueValidator(0),
                                                django.core.validators.MaxValueValidator(100)],
                                    verbose_name='rating'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='type',
            field=models.CharField(choices=[('movie', 'movie'), ('tv_show', 'tv_show')], default='movie',
                                   max_length=10, verbose_name='type'),
        ),
    ]
