# -*- coding: utf-8 -*-
from odoo import fields,models


class FarmerRegistration(models.Model):
    _name = 'ncf.farmer.registration'
    _rec_name = 'berry_number'

    image = fields.Binary('image', attachment=True,)
    name = fields.Char('Farmer`s Name')
    identification_id = fields.Char('ID NO')
    berry_number = fields.Char('Berry Number')
    bank_account_id = fields.Char('Bank Account')
    bank_name = fields.Char('Bank Name')
    address_home_id = fields.Char('Address')
    place_of_residence = fields.Char('Place of Residence')
    Status = fields.Char('Status')
    gender = fields.Selection(selection=[('male', 'Male'),
                                         ('female', 'Female')])
    marital = fields.Selection(selection=[('married', 'married'),
                                          ('single', 'single')])
    birthday = fields.Datetime('Birthday')


