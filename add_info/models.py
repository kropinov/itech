# -*- coding: utf-8 -*-
from django.db import models

class Declaration(models.Model):
    num_dec = models.CharField(
        'Номер декларации',
        primary_key = True,
        max_length = 23)    
    num_con  = models.CharField(
        'Номер контейнера',
        max_length = 11)    
    num_ship = models.CharField(
        'Номер судна',
        max_length = 4)    
    date_coming = models.DateField(
        'Дата прихода')    
    name_goods = models.CharField(
        'Наименование товара',
        max_length=20)    
    place_point = models.CharField(
        'Пункт назначения',
        max_length=15)    
    date_output = models.DateField(
        'Дата выпуска')    
    kts = models.DecimalField(
        'Сумма КТС',
        max_digits = 11,
        decimal_places = 2,
        default = 0.00)    
    notes = models.TextField()
    ## ForeingKeys 
    comp = models.ForeignKey('Company', blank = True, null = True)
       
    
    
    
    def __unicode__(self):
        return self.num_dec

class Company(models.Model):
    name = models.CharField(
        'Наименование',
        max_length=20)    
    cheef = models.CharField(
        'Директор',
        max_length=20)    
    law_adr = models.CharField(
        'Юридичский адрес',
        max_length=40)    
    pay_OGRN = models.BigIntegerField(
        'ОГРН',
        max_length=13)    
    pay_INN = models.BigIntegerField(
        'ИНН',
        max_length=10)    
    pay_KPP = models.BigIntegerField(
        'КПП',
        max_length=9)    
    pay_OKPO = models.BigIntegerField(
        'ОКПО',
        max_length=8)    
    pay_RASCH = models.BigIntegerField(
        'р/счет',
        max_length=20)    
    pay_KORR = models.BigIntegerField(
        'корр/счет',
        max_length=20)    
    pay_BIK = models.BigIntegerField(
        'БИК',
        max_length=9)    
    data_end_cert = models.DateField(
        'Дата истечения сертификата ЭЦП')

    def __unicode__(self):
        return self.name
    
class Judcase(models.Model):# Судебное дело
    dec = models.ForeignKey('declaration')
    #law = models.ForeignKey('Lawyer')
    type_of_case = models.CharField(
        'Тип дела',
        max_length=15,
        choices = [
            ('rep', 'Обжалование отказа в возврате 1'),
            ('r_not_kts', 'Обжалование отказа в возврате без КТС'),
            ('not_enter', 'Обжалование отказа в возврате Решение не вступило в силу')],
        default = 'not_enter')
    reason = models.TextField(
        'причина подачи судебного иска')
    data_to_lawyer = models.DateField(
        'дата передачи документов юристам',
        blank = True,
        null = True)
    data_pay_order = models.DateField(
        'дата платежного поручения(гос. пошлина)',
        blank = True,
        null = True)
    data_jud_sit =  models.DateField(
        'дата судебного заседания',
        blank = True,
        null = True)
    num_judmnt = models.CharField(
        'номер решения суда',
        max_length=15,
        blank = True)
    data_judmnt = models.DateField(
        'дата решения суда',
        blank = True,
        null = True)
    result_path = models.CharField(
        'результивная часть',
        max_length=15,
        blank = True,
        choices = [
            ('pass', 'Удовлетворено'),
            ('nopass', 'Неудовлетворено'),
            ('inproc', 'В процессе')],
        default = 'inproc')
    
    def __unicode__(self):
        return '%s - %s'% (self.dec_id, self.get_type_of_case_display())
    
class Plea(models.Model):
    dec = models.ForeignKey('declaration')
    reason = models.TextField(
        'причина подачи жалобы')
    inspector = models.CharField(
        'Инспектор',
        max_length=10,
        blank = True)
    data_of_plea = models.DateField(
        'дата подачи жалобы',
        blank = True,
        null = True)
    data_response = models.DateField(
        'дата ответа',
        blank = True,
        null = True)
    notes = models.TextField(
        'Примечание',
        blank=True)
    result_path = models.CharField(
        'результивная часть',
        max_length=15,
        blank = True,
        choices = [
            ('pass', 'Удовлетворено'),
            ('nopass', 'Неудовлетворено'),
            ('inproc', 'В процессе')],
        default = 'inproc')
    
    def __unicode__(self):
        return '%s - %s ... - %s' % (self.dec_id, self.reason[:20], self.get_result_path_display())    

class Lawyer(models.Model):
    judcase = models.ForeignKey('Judcase')
    #dec = models.ForeignKey('declaration')
    num_treaty = models.CharField(
        'номер договора на оказание юр. услуг',
        max_length=11,
        default = 'Не подписан')
    data_treary = models.DateField(
        'дата договора на оказание юр. услуг',
        blank = True,
        null = True)
    num_pay = models.IntegerField(
        'номер счета об оплате за оказание юр. услуг',
        max_length=4,
        blank = True,
        null = True)
    summ_pay = models.DecimalField(
        'сумма об оплате за оказание юр. услуг',
        max_digits = 6,
        decimal_places = 2,
        blank = True,
        default = 0.00)
    data_pay = models.DateField(
        'дата оплаты счета об оплате за оказание юр. услуг',
        blank = True,
        null = True)
    num_pay_order = models.IntegerField(
        'номер платежного поручения',
        max_length=3,
        blank=True,
        null = True)
    data_pay_order = models.DateField(
        'дата платежного поручения',
        blank=True,
        null = True)
    data_to_lawyer = models.DateField(
        'дата передачи документов юристам',
        blank=True,
        null = True)
    result_path = models.CharField(
        'результивная часть',
        max_length=15,
        blank=True,
        choices = [
            ('pay', 'Олачено'),
            ('notpay', 'Не оплачено')],
        default = 'notpay')  
    
    def __unicode__(self):
        return u'Договор № %s к Делу "%s"' % (self.num_treaty, self.judcase)

