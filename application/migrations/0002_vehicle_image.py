# Generated by Django 4.1.4 on 2023-01-04 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='vehicles/'),
        ),
    ]
