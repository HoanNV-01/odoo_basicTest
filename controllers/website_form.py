from odoo import http
from odoo.http import request

class WebsiteForm(http.Controller):

    @http.route('/contact/submit', type='http', auth="public", website=True)
    def contact_form_submit(self, **post):
        """Xử lý dữ liệu form khi người dùng gửi"""
        name = post.get('name')
        email = post.get('email')
        message = post.get('message')

        # Lưu thông tin vào một model (ví dụ: crm.lead)
        request.env['crm.lead'].sudo().create({
            'name': name,
            'email_from': email,
            'description': message
        })

        return request.render('my_module.contact_thank_you')
    
    @http.route('/contact', type='http', auth="public", website=True)
    def contact_page(self, **kw):
        """Hiển thị trang chứa form liên hệ"""
        return request.render('my_module.contact_page')