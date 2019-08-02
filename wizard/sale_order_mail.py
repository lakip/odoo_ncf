from odoo import models, fields, api


class OrderMail(models.TransientModel):
    _name = 'send.o.mail'
    _inherit = 'sale.order'

    recipients = fields.Char('Recipient')
    subject = fields.Char('Subject')
    body = fields.Many2many('berry.collection', string='body')

    # def open_wizard_action_id(self):
    #     pass

