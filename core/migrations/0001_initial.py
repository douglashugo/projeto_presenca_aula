# Generated by Django 4.1.7 on 2023-06-09 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Presenca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_aluno', models.CharField(max_length=100)),
                ('nome_professor', models.CharField(max_length=100)),
                ('data', models.DateField(auto_now_add=True)),
            ],
        ),
    ]