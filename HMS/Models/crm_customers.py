from  odoo import models,fields,api
from odoo.exceptions import ValidationError

class crm_customers(models.Model):
    _inherit = "res.partner"
    related_patient_id=fields.Many2one("hms.patient")
    # vat=fields.Char(required=True)

    @api.constrains('email')
    def email_validation(self):
        res=self.env['hms.patient'].search([("email","=",self.email)])
        if res :
            raise ValidationError('Email is already exists')

    @api.multi
    def unlink(self):
        for rec in self:
            if self.related_patient_id :
                raise ValidationError("You cann't delete this customer")
            else:
                super().unlink()