# Generated by Django 2.1.3 on 2019-01-12 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parseanddownload', '0002_auto_20190112_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='talksdata',
            name='Speaker',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='talksdata',
            name='Time',
            field=models.TextField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='talksdata',
            name='Topic',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='talksdata',
            name='Venue',
            field=models.TextField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='talksdata',
            name='Date',
            field=models.TextField(blank=True, max_length=20),
        ),
    ]