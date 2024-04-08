from odoo import api, fields, models, _
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta


class HmsPatient(models.Model):
    _inherit = "hms.patient"

    select_option = fields.Selection([
        ('dob', 'Date of Birth'),
        ('yob', 'Year of Birth'),
    ], string='Select')

    
    year_of_birth = fields.Integer(string='Year of Birth')

    @api.onchange('year_of_birth')
    def _onchange_year_of_birth(self):
        for patient in self:
            if patient.year_of_birth:
                current_year = date.today().year
                age = current_year - patient.year_of_birth
                patient.age = str(age) + ' Years'
            else:
                patient.age = False