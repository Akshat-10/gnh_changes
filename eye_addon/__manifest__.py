# -*- coding: utf-8 -*-
{
    'name': "my eye addons drawings",

    'summary': """
        eye me drawings me image add karna hai
        """,

    'description': """

    """,

    'author': "comp",
    'website': "https://www.yourcompany.com",


    'category': 'healthcare',
    'version': '0.1',

    'depends': ['base','acs_hms_ophthalmology','acs_hms','acs_hms_base','sltech_appointment_module','sltech_ophthalmology'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/cancel_reason_view.xml',
        'views/eye_addons.xml',
        'views/patient_add.xml',
        'views/appointment_addon.xml',
        'views/actions_ophthalmology.xml',
        'views/physician_view.xml',
        # 'views/ophthalmology_state.xml',
        'views/record_rule.xml',
        'views/appointment_button_access.xml',
    ],
    # 'assets': {
    #     'web.assets_backend': [
    #         # "eye_addon/static/src/css/style.css",
    #         # "eye_addon/static/src/components/*/*.js",
    #         # "eye_addon/static/src/js/custom.js",
    #         "eye_addon/static/src/js/ophthalmology_drawing.js",
    #     ],
    # },

}
