# Generated by Django 2.2 on 2025-05-28 20:38

from django.db import migrations, models
import myapp.utils


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_trackdatas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackdatas',
            name='track_Number',
            field=models.CharField(blank=True, default=myapp.utils.create_new_ref_number, editable=False, max_length=1000, unique=True),
        ),
    ]
