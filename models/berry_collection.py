# -*- coding: utf-8 -*-
from odoo import models,fields,api


class BerryCollection(models.Model):
    _name = 'berry.collection'

    berry_number = fields.Many2one('farmer.registration', string='Berry Number')
    first_name = fields.Char(related='berry_number.first_name', readonly=True)
    second_name = fields.Char(related='berry_number.second_name', readonly=True)
    date = fields.Datetime('Date')
    kilograms = fields.Float('Kilograms')
