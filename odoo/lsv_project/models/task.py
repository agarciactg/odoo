# -*- conding: utf-8 -*-
"""
All models from Task
"""
from odoo import models, fields

class Task(models.Model):
    """
    Task class
    """
    _inherit = 'project.task'
    _name = 'project.task'

    progress = fields.Float(string='Progress')
    task_histories_map = fields.Char(string='Map')
    sub_project_id = fields.Many2one('lsv_project.subproject'),
    qr_code_id = fields.Many2one('lsv_project.qr_code',
                                  required=False)
    task_history_ids = fields.One2many('lsv_project.task_history',
                                       'task_id')
    #planning_ids = fields.One2many('lsv_project.planning',
    #                                'task_ids')
                        