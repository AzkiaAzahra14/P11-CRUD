# Generated by Django 4.1.1 on 2022-10-06 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fakultas', '0005_dosenfaperta_nomor_dosenfeb_nomor_dosenfh_nomor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dosenfaperta',
            name='nomor',
        ),
        migrations.RemoveField(
            model_name='dosenfeb',
            name='nomor',
        ),
        migrations.RemoveField(
            model_name='dosenfh',
            name='nomor',
        ),
        migrations.RemoveField(
            model_name='dosenfisip',
            name='nomor',
        ),
        migrations.RemoveField(
            model_name='dosenfk',
            name='nomor',
        ),
        migrations.RemoveField(
            model_name='dosenft',
            name='nomor',
        ),
        migrations.RemoveField(
            model_name='dosenpascasarjana',
            name='nomor',
        ),
        migrations.RemoveField(
            model_name='mahasiswafaperta',
            name='nomor',
        ),
        migrations.RemoveField(
            model_name='mahasiswafeb',
            name='nomor',
        ),
        migrations.RemoveField(
            model_name='mahasiswafh',
            name='nomor',
        ),
        migrations.RemoveField(
            model_name='mahasiswafisip',
            name='nomor',
        ),
        migrations.RemoveField(
            model_name='mahasiswafk',
            name='nomor',
        ),
        migrations.RemoveField(
            model_name='mahasiswaft',
            name='nomor',
        ),
        migrations.RemoveField(
            model_name='mahasiswapascasarjana',
            name='nomor',
        ),
        migrations.RemoveField(
            model_name='stafffaperta',
            name='nomor',
        ),
        migrations.RemoveField(
            model_name='stafffeb',
            name='nomor',
        ),
        migrations.RemoveField(
            model_name='stafffh',
            name='nomor',
        ),
        migrations.RemoveField(
            model_name='stafffisip',
            name='nomor',
        ),
        migrations.RemoveField(
            model_name='stafffk',
            name='nomor',
        ),
        migrations.RemoveField(
            model_name='staffft',
            name='nomor',
        ),
        migrations.RemoveField(
            model_name='staffpascasarjana',
            name='nomor',
        ),
    ]