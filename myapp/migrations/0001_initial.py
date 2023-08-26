# Generated by Django 4.2.2 on 2023-08-26 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Gender', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
