# -*- coding: utf-8 -*-
from odoo import fields,models, api
from odoo.exceptions import ValidationError


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
    initials = fields.Selection(selection=[('MR', 'MR'),
                                           ('MRS', 'MRS')], onchange='onchange_gender')
    Status = fields.Char('Status')
    gender = fields.Selection(selection=[('male', 'Male'),
                                         ('female', 'Female')], readonly=True)
    marital = fields.Selection(selection=[('married', 'married'),
                                          ('single', 'single')])
    birthday = fields.Datetime('Birthday')

    @api.multi
    @api.onchange('initials')
    def onchange_gender(self):
        if self.initials == 'MR':
            self.gender = 'male'
        elif self.initials == 'MRS':
            self.gender = 'female'
        else:
            ''

    @api.constrains('name', 'berry_number')
    def check_name(self):
        for this in self:
            if self.name == self.berry_number:
                raise ValidationError('farmers name should not be same with farmers number')



