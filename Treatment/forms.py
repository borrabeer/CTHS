from datetime import datetime

from django import forms
from django.forms import ModelForm
from django.forms.widgets import (CheckboxInput, DateInput, NumberInput,
                                  RadioSelect, Select, Textarea, TextInput,
                                  TimeInput)
from django.utils.translation import gettext_lazy as _

from Treatment.models import *



class TreatmentFormDisplay(ModelForm):
    class Meta:
        model = Treatment
        exclude = ['cn', 'create_date', 'user_id', 'patient_p_id']
        labels = {
            'weight': _('น้ำหนัก'),
            'Height': _('ส่วนสูง'),
            'bp': _('ความดันโลหิต'),
            'pr': _('อัตราชีพจร'),
            'temp': _('อุณหภูมิร่างกาย'),
            'rr': _('อัตราการหายใจ'),
            'o2_sat': _('ออกซิเจนในเลือด'),
            'med_cer': _('ใบรับรองเเพทย์'),
            'patient_condition': _('สภาพผู้ป่วย'),
        }
        widgets = {
            'weight': NumberInput(attrs={'class': 'form-control', 'placeholder':'Kilograms', 'disabled': True, 'id':'weight'}),
            'Height': NumberInput(attrs={'class': 'form-control', 'placeholder':'Centimetre', 'disabled': True, 'id':'height'}),
            'bp': NumberInput(attrs={'class': 'form-control', 'placeholder':'mmHg', 'disabled': True}),
            'pr': NumberInput(attrs={'class': 'form-control', 'placeholder':'BPM','disabled': True}),
            'temp': NumberInput(attrs={'class': 'form-control', 'placeholder':'Celcuis','disabled': True}),
            'rr': NumberInput(attrs={'class': 'form-control', 'placeholder':'RPM','disabled': True}),
            'o2_sat': NumberInput(attrs={'class': 'form-control', 'placeholder':'%','disabled': True}),
            'med_cer': CheckboxInput(attrs={'class': '','disabled': True}),
            'patient_condition': RadioSelect(attrs={'class': 'form-check-input','disabled': True}),
        }

class TreatmentForm(ModelForm):
    class Meta:
        model = Treatment
        exclude = ['cn', 'create_date', 'user_id', 'patient_p_id', 'bmi']
        labels = {
            'weight': _('น้ำหนัก'),
            'Height': _('ส่วนสูง'),
            'bp': _('ความดันโลหิต'),
            'pr': _('อัตราชีพจร'),
            'temp': _('อุณหภูมิร่างกาย'),
            'rr': _('อัตราการหายใจ'),
            'o2_sat': _('ออกซิเจนในเลือด'),
            'med_cer': _('ใบรับรองเเพทย์'),
            'patient_condition': _('สภาพผู้ป่วย'),
        }
        widgets = {
            'weight': NumberInput(attrs={'class': 'form-control', 'placeholder':'Kilograms', 'id':'weight', 'v-on:blur':'bmi_cal'}),
            'Height': NumberInput(attrs={'class': 'form-control', 'placeholder':'Centimetre', 'id':'height', 'v-on:blur':'bmi_cal'}),
            'bp': NumberInput(attrs={'class': 'form-control', 'placeholder':'mmHg'}),
            'pr': NumberInput(attrs={'class': 'form-control', 'placeholder':'BPM'}),
            'temp': NumberInput(attrs={'class': 'form-control', 'placeholder':'Celcuis'}),
            'rr': NumberInput(attrs={'class': 'form-control', 'placeholder':'RPM'}),
            'o2_sat': NumberInput(attrs={'class': 'form-control', 'placeholder':'%'}),
            'med_cer': CheckboxInput(attrs={'class': ''}),
            'patient_condition': RadioSelect(attrs={'class': 'form-check-input'}),
        }

class SymptomForm(ModelForm):
    class Meta:
        model = Symptom
        exclude = ['treatment']

class Icd_10Form(ModelForm):
    class Meta:
        model = Icd_10
        fields = '__all__'

class DiagnosisForm(ModelForm):
    follow_up = forms.DateField(required=False, widget=TextInput(attrs={'class': 'form-control', 'type':'date'}))
    follow_up_for = forms.CharField(required=False, widget= TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Diagnosis
        exclude = ['treatment', 'doctor_id','icd_10']
        widgets = {
            'diagnosis_detail': Textarea(attrs={'class': 'form-control', 'rows':'7', 'cols': '4'}),
            'advice': Textarea(attrs={'class': 'form-control', 'rows':'7', 'cols': '4'}),
        }

    def clean_follow_up(self):
        current_date = datetime.now().date()
        if self.cleaned_data['follow_up']:
            if self.cleaned_data['follow_up'] <= current_date:
                raise forms.ValidationError("วันนัดไม่ถูกต้อง !")
        return self.cleaned_data['follow_up']


class Non_Form_SymptomForm(ModelForm):
    class Meta:
        model = Non_Form_Symptom
        exclude = ['symptom']
        widgets = {
            'important_symptom': Textarea(attrs={'class': 'form-control', 'rows':'15', 'cols': '4'}),
            'current_history': Textarea(attrs={'class': 'form-control', 'rows':'15', 'cols': '4'}),
        }

class Rash_SymptomForm(ModelForm):
    class Meta:
        model = Rash_Symptom
        exclude = ['symptom']
        widgets = {
            'rash_area': TextInput(attrs={'class': 'form-control'}),
            'rash_date': NumberInput(attrs={'class': 'form-control'}),
            'itch': CheckboxInput(attrs={'class': 'form-check-input'}),
            'pain': CheckboxInput(attrs={'class': 'form-check-input'}),
            'sting': CheckboxInput(attrs={'class': 'form-check-input'}),
            'fever': CheckboxInput(attrs={'class': 'form-check-input'}),
            'swell': CheckboxInput(attrs={'class': 'form-check-input'}),
            'rash_detail': TextInput(attrs={'class': 'form-control'}),    
            'pe': Textarea(attrs={'class': 'form-control', 'rows':'6', 'cols': '4'}),        
        }

class Wound_SymptomForm(ModelForm):
    class Meta:
        model = Wound_Symptom
        exclude = ['symptom']
        widgets = {
            'emergency': CheckboxInput(attrs={'class': 'form-check-input'}),
            'insurance': CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_safety': CheckboxInput(attrs={'class': 'form-check-input'}),
            'wound_area': TextInput(attrs={'class': 'form-control'}),
            'wound_date': DateInput(attrs={'class': 'form-control','type':'date'}),
            'wound_locale': TextInput(attrs={'class': 'form-control'}),
            'is_treat_before': CheckboxInput(attrs={'class': 'form-check-input'}),
            'treatment_before_detail': TextInput(attrs={'class': 'form-control'}),    
            'time': TimeInput(attrs={'class': 'form-control','type':'time'}),        
        }

class LesionForm(ModelForm):
    class Meta:
        model = Lesion
        exclude = ['wound_symptom']
        widgets = {
            'lesion_type' : Select(attrs={'class': 'custom-select'}),
            'lesion_area' : TextInput(attrs={'class': 'form-control'}),
            'lesion_x': TextInput(attrs={'class': 'form-control col-md-4'}),
            'lesion_y': TextInput(attrs={'class': 'form-control col-md-4'}),
        }

    

class Con_Wound_SymptomForm(ModelForm):
    class Meta:
        model = Con_Wound_Symptom
        exclude = ['symptom']
        widgets = {
            'insurance': CheckboxInput(attrs={'class': 'form-check-input'}),
            'detail': RadioSelect(),
            'advice': Textarea(attrs={'class': 'form-control','rows':"6", 'cols':"4"}),
            'more': Textarea(attrs={'class': 'form-control','rows':"15", 'cols':"4"})      
        }

class Eye_SymptomForm(ModelForm):
    class Meta:
        model = Eye_Symptom
        exclude = ['symptom']
        widgets = {
            'left': CheckboxInput(attrs={'class': 'form-check-input'}),
            'right': CheckboxInput(attrs={'class': 'form-check-input'}),
            'pain': CheckboxInput(attrs={'class': 'form-check-input'}),
            'irritation': CheckboxInput(attrs={'class': 'form-check-input'}),
            'itch': CheckboxInput(attrs={'class': 'form-check-input'}),
            'conjunctivitis': CheckboxInput(attrs={'class': 'form-check-input'}),
            'sore': CheckboxInput(attrs={'class': 'form-check-input'}),
            'swoll': CheckboxInput(attrs={'class': 'form-check-input'}),
            'tear': CheckboxInput(attrs={'class': 'form-check-input'}),
            'blurred': CheckboxInput(attrs={'class': 'form-check-input'}),
            'gum': CheckboxInput(attrs={'class': 'form-check-input'}),
            'purulent': CheckboxInput(attrs={'class': 'form-check-input'}),
            'matter': CheckboxInput(attrs={'class': 'form-check-input'}),
            'check_up': Textarea(attrs={'class': 'form-control mb-5','rows':"17", 'cols':"4"}) 
                    
        }

class Fever_SymptomForm(ModelForm):
    class Meta:
        model = Fever_Symptom
        exclude = ['symptom']
        widgets = {
            'fever': CheckboxInput(attrs={'class': 'form-check-input'}),
            'cough': CheckboxInput(attrs={'class': 'form-check-input'}),
            'phlegm': CheckboxInput(attrs={'class': 'form-check-input'}),
            'snot': CheckboxInput(attrs={'class': 'form-check-input'}),
            'headache': CheckboxInput(attrs={'class': 'form-check-input'}),
            'stuffy': CheckboxInput(attrs={'class': 'form-check-input'}),
            'food_bored': CheckboxInput(attrs={'class': 'form-check-input'}),
            'body_aches': CheckboxInput(attrs={'class': 'form-check-input'}),
            'sore_throat': CheckboxInput(attrs={'class': 'form-check-input'}),
            'eye_itch': CheckboxInput(attrs={'class': 'form-check-input'}),

            'injected_pharynx': CheckboxInput(attrs={'class': 'form-check-input'}),
            'exudates': CheckboxInput(attrs={'class': 'form-check-input'}),
            'lungs': CheckboxInput(attrs={'class': 'form-check-input'}),
            'more': Textarea(attrs={'class': 'form-control mb-4', 'rows':"16", 'cols':"4"})
        }

class Diarrhea_SymptomForm(ModelForm):
    class Meta:
        model = Diarrhea_Symptom
        exclude = ['symptom']
        widgets = {
            'vomit': CheckboxInput(attrs={'class': 'form-check-input'}),
            'flux_stool': CheckboxInput(attrs={'class': 'form-check-input'}),
            'fever': CheckboxInput(attrs={'class': 'form-check-input'}),
            'diarrhea_amount': NumberInput(attrs={'class': 'form-control'}),
            'diarrhea_detail': TextInput(attrs={'class': 'form-control'}),
            'stomachache': TextInput(attrs={'class': 'form-control'}),
            'bowel_sound': TextInput(attrs={'class': 'form-control'}),
            'current_history': Textarea(attrs={'class': 'form-control','rows':"15", 'cols':"4"})      
        }

class Pain_SymptomForm(ModelForm):
    class Meta:
        model = Pain_Symptom
        exclude = ['symptom']
        widgets = {
            'bodyache_area': TextInput(attrs={'class': 'form-control', 'placeholder':'บริเวณ'}),
            'bodyache_date': NumberInput(attrs={'class': 'form-control', 'placeholder':'จำนวนวัน'}),
            'pain_score': NumberInput(attrs={'class': 'form-control', 'placeholder':'0 - 10'}),
            'ache_detail': TextInput(attrs={'class': 'form-control', 'placeholder':'ลักษณะการปวด'}),
            'trigger': TextInput(attrs={'class': 'form-control', 'placeholder':'สิ่งที่กระตุ้น/สิ่งที่บรรเทา'}),
            'crack': TextInput(attrs={'class': 'form-control', 'placeholder':'ร้าวไป'}),
            'others': Textarea(attrs={'class': 'form-control', 'cols':'6', 'rows':'10', 'placeholder':'อาการอื่นๆ'}),
            
        }
