# Generated by Django 4.2.5 on 2023-09-30 16:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jobs", "0004_joblisting_location"),
    ]

    operations = [
        migrations.AddField(
            model_name="joblisting",
            name="job_url",
            field=models.CharField(max_length=500, null=True),
        ),
    ]
