# Generated by Django 4.0.6 on 2022-10-31 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0008_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='park',
            name='description',
            field=models.TextField(null=True),
        ),
    ]