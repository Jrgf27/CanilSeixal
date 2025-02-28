# Generated by Django 5.0.7 on 2025-02-24 19:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adoptante',
            old_name='morada',
            new_name='cidade',
        ),
        migrations.RemoveField(
            model_name='adoptante',
            name='mobile',
        ),
        migrations.AddField(
            model_name='adoptante',
            name='cc_expiraçao',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='adoptante',
            name='codigo_postal',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='adoptante',
            name='localidade',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='adoptante',
            name='profissao',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='adoptante',
            name='rua',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='adoptante',
            name='telefone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='adoptante',
            name='telemovel',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='adoptante',
            name='cc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='adoptante',
            name='idade',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='adoptante',
            name='nif',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='idade',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='animalimages',
            name='animal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fotos', to='mainpage.animal'),
        ),
    ]
