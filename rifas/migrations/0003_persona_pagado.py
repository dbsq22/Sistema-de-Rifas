# Generated by Django 5.0.6 on 2024-05-30 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rifas', '0002_alter_numerodisponible_numero_alter_persona_numero'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='pagado',
            field=models.BooleanField(default=False),
        ),
    ]