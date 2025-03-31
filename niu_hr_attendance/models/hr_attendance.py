from odoo import _, api, fields, models, tools

class HrAttendance(models.Model):
    _inherit= "hr.attendance"
 
    check_in_date = fields.Date(string='Data Check In', compute='_compute_check_in', store=True, readonly=True)
    check_in_time = fields.Float(string='Ora Check In', compute='_compute_check_in', store=True, readonly=True)
    check_out_date = fields.Date(string='Data Check Out', compute='_compute_check_out', store=True, readonly=True)
    check_out_time = fields.Float(string='Ora Check Out', compute='_compute_check_out', store=True, readonly=True)
 
    @api.depends('check_in')
    def _compute_check_in(self):
        for record in self:
            if record.check_in:
                record.check_in_date = record.check_in.date()
                time = fields.Datetime.context_timestamp(self, record.check_in).time()
                record.check_in_time = time.hour + time.minute / 60
            else:
                record.check_in_date = False
                record.check_in_time = False
 
    @api.depends('check_out')
    def _compute_check_out(self):
        for record in self:
            if record.check_out:
                record.check_out_date = record.check_out.date()
                time = fields.Datetime.context_timestamp(self, record.check_out).time()
                record.check_out_time = time.hour + time.minute / 60
            else:
                record.check_out_date = False
                record.check_out_time = False