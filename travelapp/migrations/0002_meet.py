# Generated by Django 4.1.4 on 2023-01-04 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='meetpic')),
                ('name', models.CharField(max_length=250)),
                ('desi', models.TextField()),
            ],
        ),
    ]
