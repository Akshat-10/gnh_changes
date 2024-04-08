from odoo import api, fields, models
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta


class AppointmentAddon(models.Model):
    _inherit = 'hms.appointment'

    select_option = fields.Selection([
        ('dob', 'Date of Birth'),
        ('yob', 'Year of Birth'),
    ], string='Select')

    year_of_birth = fields.Integer(string='Year of Birth')

    validity = fields.Integer(
        string='Validity (In Days)',
        related='physician_id.validity',
        readonly=True,
        store=True,
    )

    @api.onchange('year_of_birth')
    def _onchange_year_of_birth(self):
        for appointment in self:
            if appointment.year_of_birth:
                    current_year = date.today().year
                    age = current_year - appointment.year_of_birth
                    appointment.age = str(age) + " Years"
            else:
                self.age = 0
    
    def action_direct_to_doctor(self):
        return