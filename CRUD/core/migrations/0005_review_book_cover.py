# Generated by Django 5.1.3 on 2024-12-03 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_user_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='book_cover',
            field=models.ImageField(blank=True, null=True, upload_to='reviews/covers/'),
        ),
    ]
