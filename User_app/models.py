from datetime import datetime, date
from django.conf import settings
from django.contrib.auth.models import AbstractUser, User
from django import forms
from django.db import models
from django.forms import ModelForm
from django.forms.widgets import (DateInput, RadioSelect, Select, Textarea,
                                  TextInput)
from django.utils.translation import gettext_lazy as _

# Create your models here.

NATIONALITIES_CHOICE = [('Afghan', 'Afghan'), ('Albanian', 'Albanian'), ('Algerian', 'Algerian'), 
                     ('American', 'American'), ('Andorran', 'Andorran'), ('Angolan', 'Angolan'), 
                     ('Antiguans', 'Antiguans'), ('Argentinean', 'Argentinean'), ('Armenian', 'Armenian'), 
                     ('Australian', 'Australian'), ('Austrian', 'Austrian'), ('Azerbaijani', 'Azerbaijani'), 
                     ('Bahamian', 'Bahamian'), ('Bahraini', 'Bahraini'), ('Bangladeshi', 'Bangladeshi'), 
                     ('Barbadian', 'Barbadian'), ('Barbudans', 'Barbudans'), ('Batswana', 'Batswana'), 
                     ('Belarusian', 'Belarusian'), ('Belgian', 'Belgian'), ('Belizean', 'Belizean'), 
                     ('Beninese', 'Beninese'), ('Bhutanese', 'Bhutanese'), ('Bolivian', 'Bolivian'), 
                     ('Bosnian', 'Bosnian'), ('Brazilian', 'Brazilian'), ('British', 'British'), 
                     ('Bruneian', 'Bruneian'), ('Bulgarian', 'Bulgarian'), ('Burkinabe', 'Burkinabe'), 
                     ('Burmese', 'Burmese'), ('Burundian', 'Burundian'), ('Cambodian', 'Cambodian'), 
                     ('Cameroonian', 'Cameroonian'), ('Canadian', 'Canadian'), ('Cape Verdean', 'Cape Verdean'), 
                     ('Central African', 'Central African'), ('Chadian', 'Chadian'), ('Chilean', 'Chilean'), 
                     ('Chinese', 'Chinese'), ('Colombian', 'Colombian'), ('Comoran', 'Comoran'), 
                     ('Congolese', 'Congolese'), ('Costa Rican', 'Costa Rican'), ('Croatian', 'Croatian'), 
                     ('Cuban', 'Cuban'), ('Cypriot', 'Cypriot'), ('Czech', 'Czech'), ('Danish', 'Danish'), 
                     ('Djibouti', 'Djibouti'), ('Dominican', 'Dominican'), ('Dutch', 'Dutch'), 
                     ('Dutchman', 'Dutchman'), ('Dutchwoman', 'Dutchwoman'), ('East Timorese', 'East Timorese'), 
                     ('Ecuadorean', 'Ecuadorean'), ('Egyptian', 'Egyptian'), ('Emirian', 'Emirian'), 
                     ('Equatorial Guinean', 'Equatorial Guinean'), ('Eritrean', 'Eritrean'), 
                     ('Estonian', 'Estonian'), ('Ethiopian', 'Ethiopian'), ('Fijian', 'Fijian'), 
                     ('Filipino', 'Filipino'), ('Finnish', 'Finnish'), ('French', 'French'), 
                     ('Gabonese', 'Gabonese'), ('Gambian', 'Gambian'), ('Georgian', 'Georgian'), 
                     ('German', 'German'), ('Ghanaian', 'Ghanaian'), ('Greek', 'Greek'), 
                     ('Grenadian', 'Grenadian'), ('Guatemalan', 'Guatemalan'), ('Guinea-Bissauan', 'Guinea-Bissauan'), 
                     ('Guinean', 'Guinean'), ('Guyanese', 'Guyanese'), ('Haitian', 'Haitian'), 
                     ('Herzegovinian', 'Herzegovinian'), ('Honduran', 'Honduran'), ('Hungarian', 'Hungarian'), 
                     ('I-Kiribati', 'I-Kiribati'), ('Icelander', 'Icelander'), ('Indian', 'Indian'), 
                     ('Indonesian', 'Indonesian'), ('Iranian', 'Iranian'), ('Iraqi', 'Iraqi'), ('Irish', 'Irish'), 
                     ('Israeli', 'Israeli'), ('Italian', 'Italian'), ('Ivorian', 'Ivorian'), ('Jamaican', 'Jamaican'), 
                     ('Japanese', 'Japanese'), ('Jordanian', 'Jordanian'), ('Kazakhstani', 'Kazakhstani'), 
                     ('Kenyan', 'Kenyan'), ('Kittian and Nevisian', 'Kittian and Nevisian'), ('Kuwaiti', 'Kuwaiti'), 
                     ('Kyrgyz', 'Kyrgyz'), ('Laotian', 'Laotian'), ('Latvian', 'Latvian'), ('Lebanese', 'Lebanese'), 
                     ('Liberian', 'Liberian'), ('Libyan', 'Libyan'), ('Liechtensteiner', 'Liechtensteiner'), 
                     ('Lithuanian', 'Lithuanian'), ('Luxembourger', 'Luxembourger'), ('Macedonian', 'Macedonian'), 
                     ('Malagasy', 'Malagasy'), ('Malawian', 'Malawian'), ('Malaysian', 'Malaysian'), 
                     ('Maldivan', 'Maldivan'), ('Malian', 'Malian'), ('Maltese', 'Maltese'), 
                     ('Marshallese', 'Marshallese'), ('Mauritanian', 'Mauritanian'), ('Mauritian', 'Mauritian'), 
                     ('Mexican', 'Mexican'), ('Micronesian', 'Micronesian'), ('Moldovan', 'Moldovan'), 
                     ('Monacan', 'Monacan'), ('Mongolian', 'Mongolian'), ('Moroccan', 'Moroccan'), 
                     ('Mosotho', 'Mosotho'), ('Motswana', 'Motswana'), ('Mozambican', 'Mozambican'), 
                     ('Namibian', 'Namibian'), ('Nauruan', 'Nauruan'), ('Nepalese', 'Nepalese'), 
                     ('Netherlander', 'Netherlander'), ('New Zealander', 'New Zealander'), ('Ni-Vanuatu', 'Ni-Vanuatu'), 
                     ('Nicaraguan', 'Nicaraguan'), ('Nigerian', 'Nigerian'), ('Nigerien', 'Nigerien'), 
                     ('North Korean', 'North Korean'), ('Northern Irish', 'Northern Irish'), ('Norwegian', 'Norwegian'), 
                     ('Omani', 'Omani'), ('Pakistani', 'Pakistani'), ('Palauan', 'Palauan'), ('Panamanian', 'Panamanian'), 
                     ('Papua New Guinean', 'Papua New Guinean'), ('Paraguayan', 'Paraguayan'), ('Peruvian', 'Peruvian'), 
                     ('Polish', 'Polish'), ('Portuguese', 'Portuguese'), ('Qatari', 'Qatari'), ('Romanian', 'Romanian'), 
                     ('Russian', 'Russian'), ('Rwandan', 'Rwandan'), ('Saint Lucian', 'Saint Lucian'), ('Salvadoran', 'Salvadoran'), 
                     ('Samoan', 'Samoan'), ('San Marinese', 'San Marinese'), ('Sao Tomean', 'Sao Tomean'), ('Saudi', 'Saudi'), 
                     ('Scottish', 'Scottish'), ('Senegalese', 'Senegalese'), ('Serbian', 'Serbian'), ('Seychellois', 'Seychellois'), 
                     ('Sierra Leonean', 'Sierra Leonean'), ('Singaporean', 'Singaporean'), ('Slovakian', 'Slovakian'), 
                     ('Slovenian', 'Slovenian'), ('Solomon Islander', 'Solomon Islander'), ('Somali', 'Somali'), 
                     ('South African', 'South African'), ('South Korean', 'South Korean'), ('Spanish', 'Spanish'), 
                     ('Sri Lankan', 'Sri Lankan'), ('Sudanese', 'Sudanese'), ('Surinamer', 'Surinamer'), ('Swazi', 'Swazi'), 
                     ('Swedish', 'Swedish'), ('Swiss', 'Swiss'), ('Syrian', 'Syrian'), ('Taiwanese', 'Taiwanese'), 
                     ('Tajik', 'Tajik'), ('Tanzanian', 'Tanzanian'), ('Thai', 'Thai'), ('Togolese', 'Togolese'), 
                     ('Tongan', 'Tongan'), ('Trinidadian or Tobagonian', 'Trinidadian or Tobagonian'), ('Tunisian', 'Tunisian'), 
                     ('Turkish', 'Turkish'), ('Tuvaluan', 'Tuvaluan'), ('Ugandan', 'Ugandan'), ('Ukrainian', 'Ukrainian'), 
                     ('Uruguayan', 'Uruguayan'), ('Uzbekistani', 'Uzbekistani'), ('Venezuelan', 'Venezuelan'), 
                     ('Vietnamese', 'Vietnamese'), ('Welsh', 'Welsh'), ('Yemenite', 'Yemenite'), ('Zambian', 'Zambian'), 
                     ('Zimbabwean', 'Zimbabwean')]

class User(AbstractUser):
    phone = models.CharField(_("Phone numbers"), max_length=10)
    address = models.TextField(_("Address"))
    image_url = models.ImageField(upload_to="")
    idcard_number = models.CharField(_("ID card number"), max_length=13)
    nationality = models.CharField(_("Nationality"), max_length=25, default="", choices=NATIONALITIES_CHOICE)
    race = models.CharField(_("Race"), max_length=25, default="", choices=NATIONALITIES_CHOICE)
    def __str__(self):
        return '%s %s (%s)' %(self.first_name, self.last_name, self.id)

class Nurse(models.Model):
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_("User"), on_delete=models.CASCADE)
    department = models.CharField(_("Department"), max_length=255)
    def __str__(self):
        return '%s %s (%s)' %(self.user_id.first_name, self.user_id.last_name, self.id)

class Doctor(models.Model):
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_("User"), on_delete=models.CASCADE)
    specialized_branches = models.CharField(_("Specialized branches (Keen on)"), max_length=255)
    def __str__(self):
        return '%s %s (%s)' %(self.user_id.first_name, self.user_id.last_name, self.id)

class Public_Health(models.Model):
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_("User"), on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s (%s)' %(self.user_id.first_name, self.user_id.last_name, self.id)

class Patient(models.Model):
    p_id = models.AutoField(_("Patient ID"), primary_key=True)
    fname = models.CharField(_("Firstname"), max_length=255)
    lname = models.CharField(_("Lastname"), max_length=255)
    idcard_number = models.CharField(_("ID card number"), max_length=13, default="")
    # age = models.IntegerField(_("Age"), blank=True)
    birth_day = models.DateField(_("Birth date"), auto_now=False, auto_now_add=False)
    nationality = models.CharField(_("Nationality"), max_length=25, choices=NATIONALITIES_CHOICE, default='Thai')
    race = models.CharField(_("Race"), max_length=25, choices=NATIONALITIES_CHOICE, default='Thai')
    PATIENT_STATUS_CHOICE = [
        ('S', 'โสด'),
        ('M', 'สมรส'),
        ('O', 'อื่นๆ')
    ]
    status = models.CharField(_("Patient Condition"), max_length=1, choices=PATIENT_STATUS_CHOICE, default='1')
    PATIENT_BLOOD_TYPE_CHOICE = [
        ('A', 'A'),
        ('B', 'B'),
        ('O', 'O'),
        ('AB', 'AB')
    ]
    blood_type = models.CharField(_("Blood Type"), max_length=2, choices=PATIENT_BLOOD_TYPE_CHOICE)
    phone = models.CharField(_("Phone"), max_length=10)
    address = models.TextField(_("Address"))
    public_health_id = models.ForeignKey(Public_Health, verbose_name=_("Creator ID"), on_delete=models.SET_NULL, null=True)
    # nurse_id = models.ForeignKey(Nurse, verbose_name=_("Creator ID"), on_delete=models.SET_NULL, null=True)
    date = models.DateField(_("Created Date"), auto_now=True)
    PATIENT_ROLE_CHOICE = [
        ('1', 'นักศึกษา'),
        ('2', 'พนักงานเงินงบประมาณ'),
        ('3', 'ข้าราชการ'),
        ('4', 'พนักงานเงินได้'),
        ('5', 'ประกันสังคม'),
        ('6', 'พนักงานพิเศษ'),
        ('7', 'พนักงานเปลี่ยนสภาพ'),
        ('8', 'อื่นๆ')
    ]
    patient_role = models.CharField(_("Patient Role"), max_length=2, choices=PATIENT_ROLE_CHOICE, default='1')
    id_code = models.CharField(_("Personnal ID"), max_length=10, default="", null=True, unique=True)
    hospital_refer = models.CharField(_('Hospital Refer'), max_length=255, default="")
    gold_card_no = models.CharField(_('Gold card no.'), max_length=10, blank=True)
    gold_card_expire = models.DateField(_("Gold card expire date"), auto_now=False, auto_now_add=False, null=True, blank=True)


    def age(self):
        age_day = (date.today() - self.birth_day).days
        age_year = age_day // 365.25
        age_day -= age_year*365.25
        age_month = age_day // 30
        age_day -= age_month*30
        return int(age_year), int(age_month), int(age_day)
    age = property(age)

    def __str__(self):
        return '%s %s (%s)' %(self.fname, self.lname, self.p_id)

class Congenital_disease(models.Model):
    name = models.CharField(_("Congenital disease name"), max_length=255)
    patient_id = models.ManyToManyField(Patient, verbose_name=_("Patient ID"))
    def __str__(self):
        return '%s' %(self.name)