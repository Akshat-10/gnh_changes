from odoo import api, fields, models, _
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta


class AppointmentAddon(models.Model):
    _inherit = 'hms.appointment'

    select_option = fields.Selection([
        ('dob', 'Date of Birth'),
        ('yob', 'Year of Birth'),
    ], string='Select')

    # discount_type = fields.Selection([('fixed', 'Fixed'), ('percentage', 'Percentage')], string="Discount Type", groups='base.group_erp_manager')
    # discount = fields.Float('Discount', tracking=True, groups='base.group_erp_manager')

    year_of_birth = fields.Char(string='Year of Birth')
    
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
    

    # def action_direct_to_doctor(self):
    #     self.ensure_one()
    #     optom_id = self.env['acs.ophthalmology.evaluation'].sudo().create(
    #         {'patient_id': self.patient_id.id, 'physician_id': self.physician_id.id, 'appointment_id': self.id,
    #          'age': self.age})
    #     optom_id.onchange_patient_id_for_sltech_ophthalmology()
    #     optom_id.action_inprogress()
    #     message = _('Ophthalmology Evaluation Created.')
    #     optom_id.submit_refractive_readings_to_doctor_optometry()
    #     print(optom_id,"-----------------")
    #     return {
    #         'effect': {
    #             'fadeout': 'slow',
    #             'message': message,
    #             'type': 'rainbow_man',
    #         }
    #     }

        # self.action_ophthalmology_request_new()
        


