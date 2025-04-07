# Generated by Django 5.2 on 2025-04-06 23:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('idAula', models.AutoField(primary_key=True, serialize=False)),
                ('nomeAula', models.TextField(max_length=100)),
                ('url', models.URLField(max_length=150)),
                ('descricaoAula', models.TextField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('idMateria', models.AutoField(primary_key=True, serialize=False)),
                ('nomeMateria', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('idQuiz', models.AutoField(primary_key=True, serialize=False)),
                ('pergunta', models.TextField(max_length=150)),
                ('resposta', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Assunto',
            fields=[
                ('idAssunto', models.AutoField(primary_key=True, serialize=False)),
                ('nomeAssuntos', models.TextField(max_length=30)),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.materia')),
            ],
        ),
    ]

# Generated by Django 5.2 on 2025-04-07 00:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('idAula', models.AutoField(primary_key=True, serialize=False)),
                ('nomeAula', models.TextField(max_length=100)),
                ('url', models.URLField(max_length=150)),
                ('descricaoAula', models.TextField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('idMateria', models.AutoField(primary_key=True, serialize=False)),
                ('nomeMateria', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('idQuiz', models.AutoField(primary_key=True, serialize=False)),
                ('pergunta', models.TextField(max_length=150)),
                ('resposta', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Assunto',
            fields=[
                ('idAssunto', models.AutoField(primary_key=True, serialize=False)),
                ('nomeAssuntos', models.TextField(max_length=30)),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.materia')),
            ],
        ),
    ]
