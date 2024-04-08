from odoo import api, fields, models


class CancelReason(models.Model):
    _name = 'cancel.reason'
    _description = "Cancel Reason"

    name = fields.Char('Reason')
