from  odoo import models,fields
import datetime
class patient_logs (models.Model):
    _name = "hms.patient_logs"
    Description=fields.Text()
    patient_id=fields.Many2one(comodel_name="hms.patient")
