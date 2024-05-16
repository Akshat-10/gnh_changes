from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    validity_until = fields.Datetime(string="Valid Until", config_parameter='eye_addon.validity_until')
    valid_notify = fields.Integer(
        string="Notify Before (Days)",
        default=10,
        help="Number of days before expiration to trigger notifications.",
        config_parameter='eye_addon.valid_notify'
    )

    @api.model
    def set_values(self):
        super().set_values()
        self.env['ir.config_parameter'].set_param('eye_addon.valid_notify', str(self.valid_notify))

    @api.constrains('valid_notify')
    def _check_valid_notify(self):
        for record in self:
            print("valid_notify - ", record.valid_notify)
            print("valid_notify - ", type(record.valid_notify))
            if record.valid_notify <= 4:
                raise ValidationError("Notify Before (Days) must be at least 4.")
            
