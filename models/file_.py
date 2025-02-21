from odoo import fields, models, api

class ContractFile(models.Model):
   _name = "contract_document.file"
   _description = "Contract File"
   _rec_name = "file_name_text"  

   file_name = fields.Binary(string="Contract File", attachment=True, required=True)  # Lưu file
   file_name_text = fields.Char(string="File Name")  # Lưu tên file thực tế
   contract_id = fields.Integer(string='Contract ID', default=lambda self: self.env.user.id, readonly=True)
