# Generated by Django 5.1.3 on 2024-11-11 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_recommendation', '0003_alter_applicantprofile_resume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicantprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='jobpost',
            name='location',
        ),
        migrations.RemoveField(
            model_name='jobpost',
            name='skills',
        ),
        migrations.AddField(
            model_name='jobpost',
            name='skills_required',
            field=models.TextField(default='Not specified'),
        ),
        migrations.AlterField(
            model_name='applicantprofile',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='applicantprofile',
            name='skills',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
