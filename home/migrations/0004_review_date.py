# Generated by Django 3.2.2 on 2021-05-15 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_review_movie_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
