# Generated by Django 4.2.1 on 2023-05-16 19:16

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('q_id', models.CharField(max_length=50, primary_key=50, serialize=False)),
                ('q_no', models.IntegerField()),
                ('quiz', models.CharField(max_length=250)),
                ('q_tag', models.CharField(max_length=50, null=True, unique=True)),
                ('options', jsonfield.fields.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('survey_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('date_posted', models.DateField()),
                ('survey_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.CharField(max_length=50)),
                ('q_tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.question', to_field='q_tag')),
                ('survey_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.survey')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='survey_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.survey'),
        ),
    ]
