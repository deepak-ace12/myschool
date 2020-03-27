# Generated by Django 3.0.4 on 2020-03-27 14:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seating_capacity', models.IntegerField(default=15, validators=[django.core.validators.MinValueValidator(15)])),
                ('web_lecture_support', models.BooleanField(default=False)),
                ('shape', models.CharField(choices=[('oval', 'oval'), ('rectangular', 'rectangular'), ('canopy', 'canopy'), ('elevated', 'elevated')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Relative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=40)),
                ('contact_number', models.CharField(max_length=10)),
                ('relation', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('duration', models.IntegerField(default=30, validators=[django.core.validators.MinValueValidator(30), django.core.validators.MaxValueValidator(120)])),
                ('total_duration', models.IntegerField()),
                ('chapters', models.ManyToManyField(to='myschool.Chapter')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=40)),
                ('date_of_joining', models.DateField()),
                ('salary', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0)])),
                ('web_lecture', models.BooleanField(default=False)),
                ('subject', models.ManyToManyField(to='myschool.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=40)),
                ('date_of_joining', models.DateField()),
                ('standard', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('roll_no', models.PositiveIntegerField(unique=True)),
                ('rank', models.PositiveIntegerField()),
                ('point_of_contact', models.ManyToManyField(to='myschool.Relative')),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myschool.ClassRoom')),
                ('students', models.ManyToManyField(to='myschool.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myschool.Subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myschool.Teacher')),
            ],
        ),
    ]
