from odoo import fields, models, api

class Partner(models.Model):
  _name = 'contract_document.partner'
  _description = 'Contract Partner'
  _rec_name = 'name_partner'

  name_partner = fields.Char(string="Partner Organization Name", required=True, index=True)
  biz_rep = fields.Char(string="Business Representative", required=True)
  address = fields.Char(string="Address")
  email = fields.Char(string="Email", required=True, index=True)
  phone_number = fields.Char(string="Phone Number", required=True)
  description_partner = fields.Text(string="Description")  # Không cần required=True
  status_partner = fields.Selection([
      ('active', 'Active'),
      ('cancelled', 'Cancelled')
  ], string='Status', default='active', index=True)
  create_day_partner = fields.Datetime(string="Created Date", default=fields.Datetime.now, readonly=True, copy=False)

  @api.multi
  def toggle_status(self):
      self.ensure_one()  
      self.status_partner = 'cancelled' if self.status_partner == 'active' else 'active'