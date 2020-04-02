from  odoo import models,fields

class doctors (models.Model):
    _name="hms.doctors"
    _rec_name = "first_name"
    first_name = fields.Char()
    last_name = fields.Char()
    Image=fields.Binary(string="Image")
    patients_ids = fields.Many2many("hms.patient")