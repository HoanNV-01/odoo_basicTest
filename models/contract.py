from odoo import fields, models, api

class Contract(models.Model):
   _name = 'contract_document.contract'
   _description = 'Contract'
   _rec_name = 'name'  # Hiển thị name làm tên bản ghi

   name = fields.Char(string='Contract Name', required=True)
   partner_id = fields.Many2one('contract_document.partner', string='Partner', required=True)  # Đối tác
   contract_type_id = fields.Many2one('contract_document.type_contract', string='Contract Type', required=True)  # Loại hợp đồng
   start_date = fields.Datetime(string="Start Date", default=fields.Datetime.now, readonly=True)  # Ngày bắt đầu
   end_date = fields.Datetime(string="Expiration Date")  # Ngày hết hạn
   state = fields.Selection([
      ('active', 'Active'),
      ('expired', 'Expired'),
      ('cancelled', 'Cancelled')
   ], string="Status", default='active', required=True)  # Trạng thái hợp đồng
   contract_file_ids = fields.One2many('contract_document.file', 'contract_id', string='Attached Files')  # File hợp đồng
   note = fields.Text(string="Notes")
   
