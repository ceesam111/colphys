# Generated by Django 3.2.5 on 2022-02-25 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0005_auto_20220224_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='HOC_code',
            field=models.CharField(default=2019, max_length=4),
            preserve_default=False,
        ),
    ]
