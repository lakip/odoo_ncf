# -*- coding: utf-8 -*-
from odoo import fields,models


class Dashboard(models.Model):
    _name = 'farmer.registration'
    _rec_name = 'berry_number'

    first_name = fields.Char('First Name')
    second_name = fields.Char('Second Name')
    ID = fields.Char('ID')
    phone = fields.Char('Phone Number')
    berry_number = fields.Char('Berry Number')
