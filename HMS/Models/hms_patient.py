from  odoo import models,fields,api


class patient (models.Model):
    _name="hms.patient"
    _rec_name = "first_name"
    first_name=fields.Char()
    last_name=fields.Char()
    Birth_date=fields.Date()
    History =fields.Html()
    cd_ratio=fields.Float()
    Blood_type=fields.Selection([('o+', 'O+'), ('O-', 'o-')])
    PCR=fields.Boolean()
    Address=fields.Text()
    Age=fields.Integer()
    department_id = fields.Many2one(comodel_name="hms.department")
    department_capacity=fields.Integer(related="department_id.Capacity")
    doctors_ids=fields.Many2many("hms.doctors")
    logs_id=fields.One2many("hms.patient_logs","patient_id")
    state=fields.Selection([('Undetermined','undetermined'), ('Good','good'), ('Fair','fair'), ('Serious','serious')],default="Undetermined")
    email=fields.Char()

    @api.onchange('Age')
    def on_age_change(self):
        if self.Age ==0.00:
            self.PCR =False
        elif self.Age <30:
            self.PCR=True
            return{'warning':{'title':"warning",
                              'message':"PCR has been checked"}}

    def Status(self):
        if self.state == 'Undetermined':
            self.state='Good'
        elif self.state == 'Good':
            self.state='Fair'
        elif self.state == 'Fair':
            self.state='Serious'


    @api.onchange('state')
    def on_state_change(self):
        self.env['hms.patient_logs'].new({'Description':self.state,'patient_id':self.id})