# Generated by Django 3.2.5 on 2022-02-24 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0004_rename_user_profile_userprofileinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='matric_no',
            field=models.CharField(default=20193317, max_length=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user_type',
            field=models.CharField(choices=[('HOC', 'HOC'), ('student', 'student'), ('parent', 'parent')], default='student', max_length=10),
        ),
    ]