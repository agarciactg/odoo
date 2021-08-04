# -*- conding: utf-8 -*-
"""
All models from
"""

from odoo import models, fields

class SubProject(models.Model):
    """
    Sub Project Class
    """
    _name = "lsv_project.subproject"
    _rec_name = "name"

    project_id = fields.Many2one('project.project',
                                 string='SubProject',
                                 required=True)

    name = fields.Char(string='Name',
                       required=True)


