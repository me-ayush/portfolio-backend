# Generated by Django 3.2.16 on 2022-10-20 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificates',
            name='certificate_issue_date',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='certificates',
            name='certificate_issue_month',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='certificates',
            name='certificate_issue_year',
            field=models.IntegerField(),
        ),
    ]
