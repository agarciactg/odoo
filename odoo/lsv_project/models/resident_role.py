# -*- conding: utf-8 -*-
"""
All models from Resident Role module
"""

from odoo import models, fields

class ResidentRole(models.Model):
    """
    Resident Model class
    """
    _name = "lsv_project.resident_role"
    _rec_name = "name"
    name = fields.Char(string='Name',
                       required=True)