# Generated by Django 3.0.4 on 2020-04-06 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Genres name')),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('poster', models.ImageField(upload_to='', verbose_name='Poster')),
                ('description', models.TextField(max_length=256, verbose_name='Description')),
                ('rating', models.PositiveSmallIntegerField(blank=True)),
                ('duration', models.DurationField(verbose_name='Duration')),
                ('genres', models.ManyToManyField(related_name='films', to='films.Genre', verbose_name='Genres')),
            ],
        ),
    ]
