# Generated by Django 4.1.1 on 2022-10-05 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dosen', '0003_alter_dosen_nidn_alter_dosen_nip_alter_dosen_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dosen',
            name='nidn',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='dosen',
            name='nip',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='dosen',
            name='no',
            field=models.CharField(max_length=50),
        ),
    ]
