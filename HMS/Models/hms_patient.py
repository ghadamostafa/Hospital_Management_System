from  odoo import models,fields,api
import re
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
import datetime
from datetime import date

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
    Age=fields.Integer(compute="compute_age")
    department_id = fields.Many2one(comodel_name="hms.department")
    department_capacity=fields.Integer(related="department_id.Capacity")
    doctors_ids=fields.Many2many("hms.doctors")
    logs_id=fields.One2many("hms.patient_logs","patient_id")
    state=fields.Selection([('Undetermined','undetermined'), ('Good','good'), ('Fair','fair'), ('Serious','serious')],default="Undetermined")
    email=fields.Char()

    @api.onchange('Age')
    def on_age_change(self):
        # if self.Age ==0.00:
        #     self.PCR =False
        if self.Age <30:
            self.PCR=True
            return{'warning':{'title':"warning",
                              'message':"PCR has been checked"}}

    # @api.onchange('PCR')
    # def check_pcr(self):
    #     if self.PCR == True:
    #         self.cd_ratio=null

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

    _sql_constraints = [('valid Email','UNIQUE(email)','The email you entered already exists')]

    @api.constrains("email")
    def check_email(self):
        for rec in self:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', rec.email)
            if match == None:
                raise ValidationError('Not a valid E-mail ID')

    @api.depends('Birth_date')
    def compute_age(self):
        for rec in self:
            rec.Age= relativedelta(date.today(), rec.Birth_date).years
