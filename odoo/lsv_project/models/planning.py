# -*- conding: utf-8 -*-
"""
All models from the Planning module
"""
from odoo import models, fields

class Planning(models.Model):
    """
    Planning class
    """
    _name = "lsv_project.planning"

    _rec_name = 'state'

    state = fields.Selection([
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('finished', 'Finished'),
    ])
    start_on = fields.Date(string='Date',
                           required=True)
    end_on = fields.Date(string='Date',
                         required=True)
    responsible_id =fields.Many2one('res.partner',
                                    string='Reponsible',
                                    required=True)
    project_id = fields.Many2one('project.project',
                                 string='Project',
                                 required=True)
    task_ids = fields.Many2many('project.task')