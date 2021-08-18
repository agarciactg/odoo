# -*- conding: utf-8 -*-
"""
All models from the Addendum module
"""
import logging
from datetime import datetime
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

    @api.onchange('start_at')
    def _onchange_start_at(self):
        """
        Capture the start and validate if te value is greater to current date.
        """
        # end_at = false, para que me obligue a cambiarlo en el _onchange_end_at
        self.end_at = False
        if self.start_at and self.start_at < datetime.now().date():
            raise ValidationError("The (start at) must be great to current date")

    @api.onchange('end_at')
    @api.depends('start_at')
    def _onchange_end_at(self):
        """
        Capture the end at and validate if the value is great to start at.
        """
        if self.end_at and self.start_at and self.end_at <= self.start_at:
            raise ValidationError("The (end at) field must be great to the (start at) field.")

    @api.onchange('addendum_date')
    @api.depends('start_at', 'end_at')
    def _onchange_addendum_date(self):
        """
        Capture the addendum date and validate that this value must bet between (start at) and (end at) values
        """
        _logger.error('addendum_date: {0}'.format(self.addendum_date))
        if self.addendum_date and self.start_at and self.end_at and self.addendum_date < self.start_at and self.addendum_date > self.end_at:
            raise ValidationError("The (addendum date) field must be between (start at) and (end at) fields")

    @api.model
    def create(self, vals):
        """
        Override the default create Addemdum method
        """
        _logger.error(vals)
        return super(Addendum, self).create(vals)
