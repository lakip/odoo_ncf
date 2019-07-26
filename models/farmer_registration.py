# -*- coding: utf-8 -*-
from odoo import fields,models, api
from odoo.exceptions import ValidationError
from datetime import datetime


class FarmerRegistration(models.Model):
    _name = 'ncf.farmer.registration'
    _rec_name = 'berry_number'
    _sql_constraints = [
        ('shortcut_unique', 'unique(identification_id,berry_number)',
         'Shortcut for this id number already exists!'),
    ]

    image = fields.Binary('image', attachment=True,)
    name = fields.Char('Farmer`s Name')
    identification_id = fields.Char('ID NO')
    berry_number = fields.Char('Berry Number')
    bank_account_id = fields.Char('Bank Account')
    bank_name = fields.Char('Bank Name')
    address_home_id = fields.Char('Address')
    phone_no = fields.Char('Phone Number')
    place_of_residence = fields.Selection(selection=[('Korara', 'Korara'),
                                                     ('Kaboito', 'Koboieto'),
                                                     ('owji', 'owji')])
    initials = fields.Selection(selection=[('MR', 'MR'),
                                           ('MRS', 'MRS')], onchange='onchange_gender', default='MR')
    Status = fields.Char('Status')
    gender = fields.Selection(selection=[('male', 'Male'),
                                         ('female', 'Female')], readonly=True)
    marital = fields.Selection(selection=[('married', 'married'),
                                          ('single', 'single')])
    birthday = fields.Date('Birthday')
    current_date = fields.Date(string='Current Date', default=datetime.today())
    age = fields.Integer('Age', compute='_compute_age', readonly=1)

    # range = fields.Selection(selection=_get_range, default="1")

    @api.depends('age')
    def _compute_age(self):
        for this in self:
            f_age = this.current_date - this.birthday
            this.age = f_age

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


class Country(models.Model):
    _inherit = 'res.partner'

    country_id = fields.Many2one('res.country', string='Country',
                                 default=lambda self: self.env['res.country'].browse([114]))
