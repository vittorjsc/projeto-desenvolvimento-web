# Generated by Django 5.1.1 on 2024-10-08 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_noticia_autor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='noticia',
        ),
        migrations.AddField(
            model_name='comentario',
            name='avaliacao',
            field=models.IntegerField(default=0),
        ),
    ]