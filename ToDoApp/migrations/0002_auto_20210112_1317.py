# Generated by Django 3.1.5 on 2021-01-12 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='ToDo',
        ),
    ]
