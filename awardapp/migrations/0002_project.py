# Generated by Django 3.1.5 on 2021-01-24 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awardapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=255)),
                ('project_description', models.TextField()),
                ('project_image', models.ImageField(upload_to='projects/')),
                ('project_link', models.CharField(max_length=255)),
            ],
        ),
    ]