# -*- coding: utf-8 -*-
from odoo import models,api,fields
from  datetime import date


class Mbuni(models.Model):
    _name = 'mbuni.collection'
    _rec_name = 'berry_number'

    berry_number = fields.Many2one('ncf.farmer.registration', string='Berry Number')
    name = fields.Char(related='berry_number.name', readonly=True)
    date = fields.Datetime('Date', default=date.today())
    kilograms = fields.Many2many('mbuni.collection', relation='ncf_mbuni_collection', column1='name',
                                 column2='kilograms', string="Kilograms")

