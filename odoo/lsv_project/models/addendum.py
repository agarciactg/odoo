# -*- conding: utf-8 -*-
"""
All models from the Addendum module
"""
import logging
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
_logger = logging.getLogger(__name__)

class Addendum(models.Model):
    """
    Addendum class
    """
    _name = 'lsv_project.addendum'

    __rec_name = "name"

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

    @api.model
    def create(self, vals):
        """
        Override the default create Addemdum method
        """
        _logger.error(vals)
        return super(Addendum, self).create(vals)
