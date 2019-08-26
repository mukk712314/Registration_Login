# Generated by Django 2.0 on 2019-07-22 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Details', '0003_details_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='dataTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=15)),
                ('Password', models.CharField(max_length=25)),
            ],
        ),
        migrations.RemoveField(
            model_name='details',
            name='Qualified',
        ),
        migrations.RemoveField(
            model_name='details',
            name='Status',
        ),
        migrations.AddField(
            model_name='details',
            name='Address',
            field=models.CharField(default=5555, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='details',
            name='City',
            field=models.CharField(default=57655, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='details',
            name='Gender',
            field=models.CharField(default=567576, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='details',
            name='HighestQualification',
            field=models.CharField(default=7886, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='details',
            name='PinCode',
            field=models.IntegerField(default=6786786),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='details',
            name='School',
            field=models.CharField(default=78678678, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='details',
            name='State',
            field=models.CharField(default=7565675, max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='details',
            name='Mobile_no',
            field=models.CharField(max_length=12),
        ),
        migrations.AddField(
            model_name='datatable',
            name='link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Details.details'),
        ),
    ]