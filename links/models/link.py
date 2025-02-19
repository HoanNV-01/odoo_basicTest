# models/links.py
from odoo import models, fields

class Links(models.Model):
    _name = 'links'
    _description = 'Links Management'
    _rec_name = "name"

    name = fields.Char(string="Link Name", required=True)
    url = fields.Char(string="URL", required=True)
    description = fields.Text(string="Description")
