# Generated by Django 4.1.7 on 2023-06-09 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_presenca_nome_professor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presenca',
            name='data',
        ),
    ]
