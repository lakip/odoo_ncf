# -*- coding: utf-8 -*-
from odoo import models, fields,api
from odoo import exceptions


class Salaries(models.Model):
    _name = 'ncf.salaries'
    _rec_name = 'id_no'

    id_no = fields.Char('ID Number')
    sname = fields.Char('')
    fname = fields.Char(related='id_no.fname', readonly=True)
    salary = fields.Float(related='id_no.salary', readonly=True, compute='_compute_salary')
    amount_paid = fields.Float('Amount Paid')
    date_of_payment = fields.Datetime('Payment Date')
    description = fields.Text(string='Description')


@api.depends('salary')
def _compute_salary(self):
    for this in self:
        if this.salary > 100000:
            raise exceptions.Warning('overpayment')


