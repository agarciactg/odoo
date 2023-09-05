# -*- conding: utf-8 -*-
"""
All models from endorsement module
"""
from odoo import models, fields

class EndorsementReason(models.Model):
    """
    Endorsement class
    """
    _name = "lsv_project.endorsement_reason"
    _rec_name = 'reason'
    reason = fields.Char(string='reason',
                         required=True)