# -*- conding: utf-8 -*-
"""
All models from Endorsement module
"""

from odoo import models, fields

class Endorsement(models.Model):
    """
    Endorsement class
    """
    _name = 'lsv_project.endorsement'

    number = fields.Char(string='Number',
                         required=True)
    endorsement_reason_id = fields.Many2one('lsv_project.endorsement_reason',
                                            string='Endorsement reason',
                                            required=True)

    bail_id = fields.Many2one('lsv_project.bail',
                              string='Bail',
                              required=True)