# -*- coding: utf-8 -*-
from odoo import models,api,fields


class Employees(models.Model):
    _name = 'ncf.employees'

    fname= fields.Char('First Name')
    sname = fields.Char('Second Name')
    id_no = fields.Char('ID')
    employment_date = fields.Datetime('Employement Date')
    employee_type = fields.Char('Type of Employment')
    job_group = fields.Char('Job Group')
    salary = fields.Float('Salary')
