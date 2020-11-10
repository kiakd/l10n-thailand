from odoo import fields, models
from promptpay import qrcode


class L10nThPromptpay(models.Model):
    _inherit = 'payment.acquirer'
    qr_code_promptpay = fields.Boolean('Use PromptPay QR code')
    promptpay_id = fields.Char(
        string="PromptPay ID", help="13 digits for company's tax ID or 10 digits for mobile phone number")

    def promptpayPayload(self, data):
        return qrcode.generate_payload(self.promptpay_id, float(data))
