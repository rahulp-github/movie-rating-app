# Generated by Django 3.2.2 on 2021-05-15 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Anonymous', max_length=100)),
                ('comment', models.CharField(max_length=200, null=True)),
                ('movie_id', models.CharField(max_length=100)),
            ],
        ),
    ]
