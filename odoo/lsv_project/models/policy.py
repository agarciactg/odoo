# -*- conding: utf-8 -*-
"""
All models from Policy module
"""

from odoo import models, fields

class Policy(models.Model):
    """
    Policy Class
    """
    _name = 'lsv_project.policy'

    _rec_name = 'number'

    number = fields.Char(string='Number',
                         required=True)
    project_id = fields.Many2one('project.project',
                                 string='Project',
                                 required=True)
    policy_type_id = fields.Many2one('lsv_project.policy_type',
                                     string='Policy_Type',
                                     required=True)
                                