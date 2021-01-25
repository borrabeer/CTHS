# Generated by Django 3.1.5 on 2021-01-25 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Con_Wound_Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance', models.BooleanField(default=False, verbose_name='ผู้ป่วยเบิกประกัน')),
                ('detail', models.CharField(choices=[('1', 'เเย่ลง'), ('2', 'เท่าเดิม'), ('3', 'ดีขึ้น')], default='2', max_length=1, verbose_name='ลักษณะบาดเเผล')),
                ('advice', models.CharField(blank=True, max_length=100, verbose_name='คำเเนะนำ')),
                ('more', models.CharField(max_length=100, verbose_name='เพิ่มเติ่ม')),
            ],
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis_detail', models.CharField(blank=True, max_length=255, verbose_name='คำวินิฉัย')),
                ('advice', models.CharField(blank=True, max_length=255, verbose_name='คำเเนะนำ')),
                ('follow_up', models.DateField(null=True, verbose_name='วันนัด')),
                ('follow_up_for', models.CharField(blank=True, max_length=100, verbose_name='เพื่อ')),
            ],
        ),
        migrations.CreateModel(
            name='Diarrhea_Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diarrhea_amount', models.IntegerField(default=0, verbose_name='จำนวนครั้งในการถ่าย')),
                ('diarrhea_detail', models.CharField(blank=True, default='', max_length=255, verbose_name='อุจจาระลักษณะ')),
                ('stomachache', models.CharField(blank=True, default='', max_length=255, verbose_name='ลักษณะการปวดท้อง')),
                ('vomit', models.BooleanField(default=False, verbose_name='คลื่นไส้/อาเจียน')),
                ('flux_stool', models.BooleanField(default=False, verbose_name='อุจาระมีมูลเลือด')),
                ('fever', models.BooleanField(default=False, verbose_name='ไข้')),
                ('bowel_sound', models.CharField(blank=True, default='', max_length=255, verbose_name='bowel sound')),
                ('current_history', models.CharField(blank=True, default='', max_length=255, verbose_name='ประวัติปัจจุบัน')),
            ],
        ),
        migrations.CreateModel(
            name='Eye_Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left', models.BooleanField(default=False, verbose_name='ตาซ้าย')),
                ('right', models.BooleanField(default=False, verbose_name='ตาขวา')),
                ('pain', models.BooleanField(default=False, verbose_name='ปวดตา')),
                ('irritation', models.BooleanField(default=False, verbose_name='เคืองตา')),
                ('itch', models.BooleanField(default=False, verbose_name='คันตา')),
                ('conjunctivitis', models.BooleanField(default=False, verbose_name='ตาเเดง')),
                ('sore', models.BooleanField(default=False, verbose_name='เจ็บหนังตา')),
                ('swoll', models.BooleanField(default=False, verbose_name='หนังตาบวม')),
                ('tear', models.BooleanField(default=False, verbose_name='น้ำตาไหล')),
                ('blurred', models.BooleanField(default=False, verbose_name='ตาพร่ามัว')),
                ('gum', models.BooleanField(default=False, verbose_name='ขี้ตาเยอะ')),
                ('purulent', models.BooleanField(default=False, verbose_name='ขี้ตาเป็นหนอง')),
                ('matter', models.BooleanField(default=False, verbose_name='สิ่งเเปลกปลอมเข้าดวงตา')),
                ('check_up', models.CharField(blank=True, max_length=255, verbose_name='ตรวจร่างกาย')),
            ],
        ),
        migrations.CreateModel(
            name='Fever_Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fever', models.BooleanField(verbose_name='ไข้')),
                ('cough', models.BooleanField(verbose_name='ไอ')),
                ('phlegm', models.BooleanField(verbose_name='เสมหะ')),
                ('snot', models.BooleanField(verbose_name='น้ำมูก')),
                ('headache', models.BooleanField(verbose_name='ปวดศีรษะ')),
                ('stuffy', models.BooleanField(verbose_name='คัดจมูก')),
                ('food_bored', models.BooleanField(verbose_name='เบื่ออาหาร')),
                ('body_aches', models.BooleanField(verbose_name='ปวดเมื่อยตามตัว')),
                ('sore_throat', models.BooleanField(verbose_name='เจ็บคอ')),
                ('eye_itch', models.BooleanField(verbose_name='คันตา')),
                ('injected_pharynx', models.BooleanField(verbose_name='Injected pharynx')),
                ('exudates', models.BooleanField(verbose_name='Exudates')),
                ('lungs', models.BooleanField(verbose_name='Lungs : Clear')),
                ('more', models.CharField(blank=True, max_length=255, verbose_name='เพิ่มเติ่ม')),
            ],
        ),
        migrations.CreateModel(
            name='Icd_10',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=25, unique=True, verbose_name='code')),
                ('detail', models.CharField(max_length=255, verbose_name='detail')),
                ('symptom_type', models.CharField(choices=[('non_form', 'ทั่วไป'), ('skin', 'ผิวหนัง'), ('accident', 'อุบัติเหตุ'), ('con_accident', 'อุบัติเหตุต่อเนื่อง'), ('eyes', 'ดวงตา'), ('fever', 'อาการไข้'), ('diarrhea', 'ท้องเสีย/ปวดท้อง'), ('pain', 'อาการปวดนอกเหนือ')], max_length=12, verbose_name='symptom_type')),
            ],
        ),
        migrations.CreateModel(
            name='Lesion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesion_type', models.CharField(choices=[('1', 'ถลอก'), ('2', 'ฉีกขาด'), ('3', 'จากของมีคม'), ('4', 'อื่นๆ')], max_length=1, verbose_name='บาดแผล')),
                ('lesion_area', models.CharField(max_length=100, verbose_name='บริเวณ')),
                ('lesion_x', models.IntegerField(verbose_name='กว้าง')),
                ('lesion_y', models.IntegerField(verbose_name='ยาว')),
            ],
        ),
        migrations.CreateModel(
            name='Non_Form_Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('important_symptom', models.CharField(max_length=255, verbose_name='อาการสำคัญ')),
                ('current_history', models.CharField(max_length=255, verbose_name='ประวัติปัจจุบัน')),
            ],
        ),
        migrations.CreateModel(
            name='Pain_Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bodyache_area', models.CharField(max_length=255, verbose_name='ปวดบริเวณ')),
                ('bodyache_date', models.IntegerField(verbose_name='เป็นมานาน (วัน)')),
                ('pain_score', models.IntegerField(verbose_name='Pain score')),
                ('ache_detail', models.CharField(max_length=255, verbose_name='ลักษณะการปวด')),
                ('trigger', models.CharField(max_length=255, verbose_name='สิ่งที่กระตุ้น/สิ่งที่บรรเทา')),
                ('crack', models.CharField(max_length=255, verbose_name='ร้าวไป')),
                ('others', models.CharField(max_length=255, verbose_name='อาการอื่น')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(blank=True, max_length=255, verbose_name='Prescription detail')),
                ('status', models.CharField(choices=[('C', 'จ่ายยาแล้ว'), ('W', 'รอการจ่ายยา')], default='W', max_length=1, verbose_name='Prescription Status')),
            ],
        ),
        migrations.CreateModel(
            name='Rash_Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rash_area', models.CharField(max_length=255, verbose_name='ผื่นบริเวณ')),
                ('rash_date', models.IntegerField(default=1, verbose_name='เป็นมานาน (วัน)')),
                ('itch', models.BooleanField(default=False, verbose_name='คัน')),
                ('pain', models.BooleanField(default=False, verbose_name='ปวด')),
                ('sting', models.BooleanField(default=False, verbose_name='เเสบ')),
                ('fever', models.BooleanField(default=False, verbose_name='ไข้')),
                ('swell', models.BooleanField(default=False, verbose_name='บวม')),
                ('rash_detail', models.CharField(max_length=255, verbose_name='สัมผัสโดน')),
                ('pe', models.CharField(max_length=255, verbose_name='PE')),
            ],
        ),
        migrations.CreateModel(
            name='Room_Queue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('WD', 'รอเข้าห้องตรวจ'), ('WP', 'รอการจ่ายยา')], default='WD', max_length=2, verbose_name='Queue status')),
            ],
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptom_type', models.CharField(choices=[('non_form', 'ทั่วไป'), ('skin', 'ผิวหนัง'), ('accident', 'อุบัติเหตุ'), ('con_accident', 'อุบัติเหตุต่อเนื่อง'), ('eyes', 'ดวงตา'), ('fever', 'อาการไข้'), ('diarrhea', 'ท้องเสีย/ปวดท้อง'), ('pain', 'อาการปวดนอกเหนือ')], max_length=12, null=True, verbose_name='symptom_type')),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('cn', models.AutoField(primary_key=True, serialize=False, verbose_name='Clinic number')),
                ('weight', models.FloatField(verbose_name='Weight')),
                ('Height', models.FloatField(verbose_name='Height')),
                ('bp', models.IntegerField(verbose_name='Blood pressures')),
                ('pr', models.IntegerField(verbose_name='Pulse rates')),
                ('temp', models.FloatField(verbose_name='Temperatures')),
                ('rr', models.IntegerField(verbose_name='Respiratory rates')),
                ('o2_sat', models.IntegerField(verbose_name='Oxygen saturation')),
                ('med_cer', models.BooleanField(verbose_name='Medical certificate')),
                ('patient_condition', models.CharField(choices=[('SC', 'มาด้วยตนเอง'), ('AB', 'รถพยาบาล'), ('ST', 'เปลนอน')], default='SC', max_length=2, verbose_name='Patient Condition')),
                ('create_date', models.DateField(auto_now=True, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Wound_Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emergency', models.BooleanField(default=False, verbose_name='ผู้ป่วยฉุกเฉิน')),
                ('insurance', models.BooleanField(default=False, verbose_name='เบิกประกันอุบัติเหตุ')),
                ('is_safety', models.BooleanField(default=False, verbose_name='สวมหมวกันน็อค/คาดเข็มขัด')),
                ('wound_area', models.CharField(max_length=255, verbose_name='บาดเเผลบริเวณ')),
                ('wound_date', models.DateField(verbose_name='วันที่เกิดเหตุ')),
                ('wound_locale', models.CharField(max_length=255, verbose_name='สถานที่เกิดเหตุ')),
                ('is_treat_before', models.BooleanField(default=False, verbose_name='เคยเข้ารับการรักมาเเล้ว')),
                ('treatment_before_detail', models.CharField(blank=True, max_length=255, verbose_name='ที่')),
                ('time', models.TimeField(blank=True, verbose_name='เวลา')),
                ('symptom', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Treatment.symptom', verbose_name='Symptom ID')),
            ],
        ),
    ]
