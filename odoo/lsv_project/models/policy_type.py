# -*- conding: utf-8 -*-
"""
All models from police type module
"""

from odoo import models, fields

class PolicyType(models.Model):
    """
    Policy Type model
    """
    _name = "lsv_project.policy_type"
    _rec_name = "name"
    name = fields.Char(string="Nombre",
                       required=True)