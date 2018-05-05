# Generated by Django 2.0.5 on 2018-05-04 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='current_school_grade',
            field=models.CharField(choices=[('幼末', '幼末'), ('幼小', '幼小'), ('幼中', '幼中'), ('幼大', '幼大'), ('小一', '小一'), ('小二', '小二')], default='幼末', max_length=2),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('BOY', 'Boy'), ('GIRL', 'Girl')], default='BOY', max_length=2),
        ),
    ]