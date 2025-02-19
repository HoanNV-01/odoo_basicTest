from odoo import fields, models, api

class Employee(models.Model):
   _name = 'employee'
   _description = 'Employee'
   _rec_name = 'full_name'

   full_name = fields.Char(string='Full Name', required=True)
   email = fields.Char(string='Email', required=True)
   password = fields.Char(string='Password', required=True)
   role = fields.Selection([
                              ('manager','Manager'),
                              ('employee','Employee'),
                              ('admin','Admin')
                           ],string='Role', default='employee')

     
   