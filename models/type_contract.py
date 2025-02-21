from odoo import fields, models, api

class Type_Contract(models.Model):
  _name = 'contract_document.type_contract'
  _description = 'Type contract'
  _rec_name = 'name_type_contract'
  
  name_type_contract = fields.Char(string="Name", required=True)
  description_type_contract = fields.Text(string="Description", required=True)
  status_type_contract = fields.Selection([
                            ('active', 'Active'),
                            ('cancelled', 'Cancelled')
                          ], string='Status', default='active')
  create_day_type_contract = fields.Datetime(string="Created Date", default=fields.Datetime.now, readonly=True)