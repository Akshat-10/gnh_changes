from odoo import models, fields, api, SUPERUSER_ID
import base64
import os

class TcbOphthalmology(models.Model):
    _inherit = "acs.ophthalmology.evaluation"


    image = fields.Binary(string="Image")


    
    state = fields.Selection([('draft', 'Draft'),
        ('in_progress', 'Under Evaluation'),
        ('confirm', 'Submitted'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
        ], 'Status', default="draft", readonly=True)

    def action_cancel(self):
        self.write({'state': 'cancel'})
        return True
    

    def action_inprogress(self):
        res = super(TcbOphthalmology, self).action_inprogress()
        self.state = 'in_progress'

    def submit_refractive_readings_to_doctor_optometry(self):
        res = super(TcbOphthalmology, self).submit_refractive_readings_to_doctor_optometry()
        self.state = 'confirm'

    def action_direct_to_doctor(self):
        self.action_inprogress()
        self.submit_refractive_readings_to_doctor_optometry()
        # self.state = 'confirm'

    # # @api.model
    # # def create(self, vals):
    # #     if vals.get('state') == 'cancel':
    # #         vals.update({'state': 'cancel'})
    # #     return super(SltechOphthalmology, self).create(vals)

    # def action_cancel(self):
    #     self.write({'state': 'cancel'})
    #     return True

    # @api.model
    # def default_get(self, fields):
    #     res = super(SltechOphthalmology, self).default_get(fields)

    #     image_path2 = os.path.join(
    #         os.path.dirname(__file__),
    #         '..',
    #         'static',
    #         'description',
    #         'eye_diagram.png'
    #     )
    #     with open(image_path2, 'rb') as f:
    #         image_data2 = base64.b64encode(f.read())
    #     self.eye_drawing_le_re2 = image_data2
    #     res['eye_drawing_le_re2'] = image_data2
    #     return res
    

################### loading recode rules custom code ##################3
    # @api.model
    # def _register_hook(self):
    #     self._load_record_rules()

    # def _load_record_rules(self):
    #     xml_file = 'eye_addon/views/record_rule.xml'  # Path to your XML file
    #     with open(xml_file, 'r') as f:
    #         xml_data = f.read()
    #     self.env['ir.model.data'].xmlid_to_object('eye_addon.custom_record_rule_ophthalmology_evaluation')._update_xmlid(xml_data)


