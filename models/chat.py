from odoo import models, fields, api
import smtplib
from email.mime.text import MIMEText
import datetime


class Chat(models.Model):
    _name = "student.manager.chat"
    _description = "Chat model"
    _rec_name = 'email'  # Định nghĩa giá trị hiển thị khi tìm kiếm
    
    email = fields.Char(string='Email', required=True)
    subject = fields.Char(string = 'Subject', required=True)
    text = fields.Text(string="Message Content")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('failed', 'Failed')
    ], string="Status", default='draft')
    
    # Send Mail
    def send_email(self):
        for record in self:
            try:
                sender = "kariatnguyen+spam@gmail.com"
                password = "vdfo ilek uknu dhuy"
                recipient = record.email
                subject = record.subject
                body = record.text
                msg = MIMEText(body, "html")
                msg["Subject"], msg["From"], msg["To"] = subject, sender, recipient

                with smtplib.SMTP("smtp.gmail.com", 587) as server:
                    server.starttls()
                    server.login(sender, password)
                    server.sendmail(sender, recipient, msg.as_string())
                record.state = 'sent'
                # Tạo thông báo hiển thị sau khi gửi email thành công
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'title': 'Success!',
                        'message': 'Email đã gửi thành công!',
                        'sticky': False,  # Set sticky = False để thông báo tự động biến mất sau một thời gian
                    },
                }
                
            except Exception as e:
                record.state = 'failed'
                print(f'Sent mail error: {e}')
                raise UserError(f"Failed to send email: {str(e)}")
                
                
                
    