# Generated by Django 4.2.2 on 2023-07-26 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=20)),
                ('Lastname', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=30)),
                ('Salary', models.IntegerField()),
            ],
        ),
    ]
