# Generated by Django 3.1.1 on 2022-12-19 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(default=None, max_length=255, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('height', models.CharField(blank=True, max_length=12)),
                ('weight', models.CharField(blank=True, max_length=12)),
                ('disease_history', models.CharField(blank=True, max_length=200)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('birthdate', models.DateField()),
                ('blood_group', models.CharField(blank=True, choices=[('gol_A', 'A'), ('gol_B', 'B'), ('gol_O', 'O'), ('gol_AB', 'AB')], max_length=10)),
                ('gender', models.CharField(blank=True, choices=[('laki-laki', 'Laki-laki'), ('perempuan', 'Perempuan')], max_length=10)),
                ('about', models.TextField(blank=True, max_length=500, null=True)),
                ('groups', models.ManyToManyField(blank=True, null=True, to='groups.Group')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
