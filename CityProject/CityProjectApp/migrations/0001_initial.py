# Generated by Django 2.0.6 on 2019-03-07 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='')),
                ('name', models.CharField(default='', max_length=20)),
                ('dropbox', models.CharField(max_length=200)),
                ('checkbox', models.CharField(max_length=200)),
                ('email', models.EmailField(default='', max_length=254)),
                ('cityoforgin', models.CharField(max_length=200)),
                ('richorsuperpowers', models.CharField(max_length=200)),
            ],
        ),
    ]
