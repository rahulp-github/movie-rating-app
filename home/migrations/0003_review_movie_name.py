# Generated by Django 3.2.2 on 2021-05-15 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_review_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='movie_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
