# -*- coding: utf-8 -*-
from odoo import models,fields,api


class BerryCollection(models.Model):
    _name = 'berry.collection'
    _rec_name = 'berry_number'

    berry_number = fields.Many2one('ncf.farmer.registration', string='Berry Number')
    name = fields.Char(related='berry_number.name', readonly=True)
    date = fields.Datetime('Date')
    kilograms = fields.Float('Kilograms')
