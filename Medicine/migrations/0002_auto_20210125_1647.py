# Generated by Django 3.1.5 on 2021-01-25 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Medicine', '0001_initial'),
        ('Treatment', '0001_initial'),
        ('User_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='patient',
            field=models.ManyToManyField(to='User_app.Patient', verbose_name='Allergic Drug(s)'),
        ),
        migrations.AddField(
            model_name='dispense',
            name='dis_drug_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Medicine.drug', verbose_name='Dispense ID'),
        ),
        migrations.AddField(
            model_name='dispense',
            name='dis_med_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Medicine.med_supply', verbose_name='Dispense ID'),
        ),
        migrations.AddField(
            model_name='dispense',
            name='prescription_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Treatment.prescription', verbose_name='Prescription ID'),
        ),
    ]
