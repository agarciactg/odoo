# -*- conding: utf-8 -*-
"""
All models from the Addendum module
"""

from odoo import models, fields

class Addendum(models.Model):
    """
    Addendum class
    """
    _name = 'lsv_project.addendum'

    number = fields.Char(string='Number',
                         required=True)
    comments = fields.Text(string='comments',
                          required=False)
    start_at = fields.Date(string='Start At',
                           required=True)
    end_at = fields.Date(string='End At',
                         required=True)
    addendum_date = fields.Date(string='Addebdum Date',
                                required=False)
    project_id = fields.Many2one('project.project',
                              string='Project',
                              required=True)
    addendum_description_id = fields.Many2one('lsv_project.addendum_description',
                                            string='Description',
                                            required=True)
    
