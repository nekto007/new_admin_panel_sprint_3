# Generated by Django 3.2 on 2022-02-04 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_person_birth_date'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='genrefilmwork',
            index=models.Index(fields=['genre'], name='genre_film_work_genre_idx'),
        ),
        migrations.AddIndex(
            model_name='genrefilmwork',
            index=models.Index(fields=['film_work'], name='genre_film_work_film_work_idx'),
        ),
        migrations.AddIndex(
            model_name='personfilmwork',
            index=models.Index(fields=['person'], name='person_film_work_person_idx'),
        ),
        migrations.AddIndex(
            model_name='personfilmwork',
            index=models.Index(fields=['film_work'], name='person_film_work_film_work_idx'),
        ),
        migrations.AddConstraint(
            model_name='genrefilmwork',
            constraint=models.UniqueConstraint(fields=('film_work', 'genre'), name='unique_film_work_genre'),
        ),
        migrations.AddConstraint(
            model_name='personfilmwork',
            constraint=models.UniqueConstraint(fields=('person', 'film_work', 'role'), name='unique_film_work_member'),
        ),
    ]
