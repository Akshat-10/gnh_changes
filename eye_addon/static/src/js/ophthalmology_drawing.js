/** @odoo-module */

import { FormController } from '@web/views/form/form_controller';
import { patch } from "@web/core/utils/patch";

patch(FormController.prototype, 'eye_addon', {
    setup() {
        this._super();
        if (this.props.resModel=='acs.ophthalmology.evaluation'){
            this.onNotebookPageChange = (notebookId, page) => {
                    $('#custom_open_draw_canvas').click(function(e) {
                        alert('Custom button clicked');
                        //  e.preventDefault();
                        // setupCanvas();
                        // $('#custom_draw_image').show()
                    });
            };
        }
    }
});