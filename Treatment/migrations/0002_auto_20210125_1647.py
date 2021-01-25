# Generated by Django 3.1.5 on 2021-01-25 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Treatment', '0001_initial'),
        ('User_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='patient_p_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User_app.patient', verbose_name='PatientID'),
        ),
        migrations.AddField(
            model_name='treatment',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creator user'),
        ),
        migrations.AddField(
            model_name='symptom',
            name='treatment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Treatment.treatment', verbose_name='Treatment'),
        ),
        migrations.AddField(
            model_name='room_queue',
            name='treatment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Treatment.treatment', verbose_name='Treatment ID'),
        ),
        migrations.AddField(
            model_name='rash_symptom',
            name='symptom',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Treatment.symptom', verbose_name='Symptom ID'),
        ),
        migrations.AddField(
            model_name='prescription',
            name='doctor_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='User_app.doctor', verbose_name='Creator ID'),
        ),
        migrations.AddField(
            model_name='prescription',
            name='nurse_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='User_app.nurse', verbose_name='พยาบาลผู้จ่ายยา'),
        ),
        migrations.AddField(
            model_name='prescription',
            name='treatment_cn',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Treatment.treatment', verbose_name='Treatment Clinic number'),
        ),
        migrations.AddField(
            model_name='pain_symptom',
            name='symptom',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Treatment.symptom', verbose_name='Symptom ID'),
        ),
        migrations.AddField(
            model_name='non_form_symptom',
            name='symptom',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Treatment.symptom', verbose_name='Symptom ID'),
        ),
        migrations.AddField(
            model_name='lesion',
            name='wound_symptom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Treatment.wound_symptom'),
        ),
        migrations.AddField(
            model_name='fever_symptom',
            name='symptom',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Treatment.symptom', verbose_name='Symptom ID'),
        ),
        migrations.AddField(
            model_name='eye_symptom',
            name='symptom',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Treatment.symptom', verbose_name='Symptom ID'),
        ),
        migrations.AddField(
            model_name='diarrhea_symptom',
            name='symptom',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Treatment.symptom', verbose_name='Symptom ID'),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='doctor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User_app.doctor', verbose_name='Diagnos Doctor'),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='icd_10',
            field=models.ManyToManyField(to='Treatment.Icd_10', verbose_name='icd_10s'),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='treatment',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Treatment.treatment', verbose_name='Treatment ID'),
        ),
        migrations.AddField(
            model_name='con_wound_symptom',
            name='symptom',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Treatment.symptom', verbose_name='Symptom ID'),
        ),
    ]
