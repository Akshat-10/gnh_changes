# coding: utf-8

from odoo import models, api, fields


class AcsCancelReasonWiz(models.TransientModel):
    _name = 'cancel.reason.wizard'


    cancel_reason_id = fields.Many2one('cancel.reason', string='Cancellation Reason', required=True)
    cancel_reason = fields.Text(string="Reason", required=True)

    
    def wizard_cancel(self):
        ophthalmology = self.env['acs.ophthalmology.evaluation'].search([('id','=',self.env.context.get('active_id'))])

        ophthalmology.action_cancel()
        print('88888888888888----------------ophthalmology-------------------888888888', ophthalmology)
        # self.write({'state': 'cancel'})
        return True
