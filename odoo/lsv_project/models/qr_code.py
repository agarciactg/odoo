# -*- conding: utf-8 -*-
"""
All from Qr code module
"""
import random
from odoo import models, fields

class QrCode(models.Model):
    """
    Qr Code model
    this model service Qr code for
    porjects and tasks
    """
    _name = "lsv_project.qr_code"

    def _compute_qr_token(self):
        return random.randrange(1000000, 9999999, 2)

    code = fields.Binary(required=False,
                        string='Qr Code')
    filename = fields.Char(string='Filename',
                           required=False)
    token = fields.Integer(string='Token',
                           default =_compute_qr_token)
