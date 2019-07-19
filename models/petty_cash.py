# -*- coding: utf-8 -*-
from odoo import models,api,fields


class PettyCash(models.Model):
    _name = 'ncf.petty.cash'

    receipt_number = fields.Char('Receipt Number')
    date = fields.Datetime('Date')
    amount = fields.Float('Amount')
    description = fields.Text(string='Description')