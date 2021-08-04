# -*- conding: utf-8 -*-
"""
All models from Bail module
"""

from odoo import models, fields

class Bail(models.Model):
    """
    Bail class
    """
    _name = 'lsv_project.bail'
    
    number = fields.Char(string='Number',
                         required=True)
    issue_date = fields.Date(string='Issue Date',
                            required=True)
    expired_at = fields.Date(string='Expired At',
                            required=True)
    insurer_id = fields.Many2one('res.partner',
                                 string='Insurer',
                                 required=True)
    project_id = fields.Many2one('project.project',
                                 string='Project',
                                  required=True)
    endorsement_ids = fields.One2many('lsv_project.endorsement',
                                     'bail_id',
                                     string='Endorsements')