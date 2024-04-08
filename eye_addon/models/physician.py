from odoo import api, fields, models, _


class HmsPhysician(models.Model):
    _inherit = "hms.physician"


    validity = fields.Integer(string='Validity (In Days)')