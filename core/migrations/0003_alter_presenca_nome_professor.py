# Generated by Django 4.1.7 on 2023-06-09 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_professor_alter_presenca_nome_professor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presenca',
            name='nome_professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='presencas', to='core.professor'),
        ),
    ]
