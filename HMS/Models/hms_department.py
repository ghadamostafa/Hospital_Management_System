from  odoo import models,fields

class department (models.Model):
    _name="hms.department"
    _rec_name="Name"
    Name=fields.Char()
    Is_opened=fields.Boolean()
    Capacity=fields.Integer()
    Patients_ids = fields.One2many("hms.patient", "department_id")