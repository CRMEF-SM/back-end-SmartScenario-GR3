# Generated by Django 4.2.1 on 2023-06-16 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sceanarios', '0002_alter_objectifs_scenario_scenarioactivity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scenarioactivity',
            name='scenario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Scenario', to='Sceanarios.scenario'),
        ),
        migrations.CreateModel(
            name='ImageScenario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.CharField(max_length=255)),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Scenarioimages', to='Sceanarios.scenario')),
            ],
        ),
    ]