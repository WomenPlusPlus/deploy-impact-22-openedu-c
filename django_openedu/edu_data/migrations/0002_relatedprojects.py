# Generated by Django 4.1 on 2022-11-01 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatedProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('similarity', models.JSONField(null=True)),
            ],
        ),
    ]
