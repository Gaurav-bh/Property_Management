# Generated by Django 3.0 on 2020-03-31 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='home/')),
                ('title', models.CharField(max_length=10)),
                ('des', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='home',
        ),
    ]
