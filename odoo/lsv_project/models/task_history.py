# -*- conding: utf-8 -*-
"""
All models from TaskHistory module
"""
from odoo import models, fields

class TaskHistory(models.Model):
    """
    TaskHistory class
    """
    _name = "lsv_project.task_history"
    
    _rec_name = "date"

    date = fields.Date(string='Date',
                        required=True)
    time = fields.Char(string='Trime',
                       required=True)
    comments = fields.Char(string='comments')
    latitude = fields.Float(string='Latitude',
                           required=True)
    longitud = fields.Float(string='Longitude',
                            required=True)
    state = fields.Selection([
        ('normal', 'Normal'),
        ('done', 'Done'),
        ('blocked', 'Blocked')
    ])
    task_id = fields.Many2one('project.task',
                              required=True)