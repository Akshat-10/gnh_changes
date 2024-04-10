from odoo import api, fields, models, _
from datetime import date, datetime, timedelta
# from dateutil.relativedelta import relativedelta


class HmsPatient(models.Model):
    _inherit = "hms.patient"

    select_option = fields.Selection([
        ('dob', 'Date of Birth'),
        ('yob', 'Year of Birth'),
    ], string='Select')

    year_of_birth = fields.Char(string='Year of Birth')


    @api.onchange('year_of_birth')
    def _onchange_year_of_birth(self):
        for appointment in self:
            if appointment.year_of_birth:
                try:
                    birth_year_int = int(appointment.year_of_birth)
                    current_year = fields.Date.today().year
                    age = current_year - birth_year_int
                    appointment.age = str(age) + " Years"
                except ValueError:
                    appointment.year_of_birth = False
                    appointment.age = False
            else:
                appointment.age = False