# Generated by Django 2.0.5 on 2018-05-04 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20180504_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('BOY', 'Boy'), ('GIRL', 'Girl')], default='BOY', max_length=5),
        ),
    ]
