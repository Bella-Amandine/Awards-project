# Generated by Django 3.1.5 on 2021-01-30 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awardapp', '0006_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_link',
            field=models.URLField(),
        ),
    ]