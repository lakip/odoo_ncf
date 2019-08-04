from odoo import models, fields, api


class BerryCollectionMessage(models.TransientModel):
    _name = 'send.collection.message'

    line_ids = fields.Many2many('mbuni.collection')

    @api.multi
    def action_send_mail(self):
        for this in self.line_ids:
            body = "This is to confirm receipt of your order!"
            this.message_post(subtype=False, body=body)
