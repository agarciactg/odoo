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
    addendum_date = fields.Date(string='Addendum Date',
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
        if self.addendum_date and self.start_at and self.end_at and self.addendum_date < self.start_at or self.addendum_date > self.end_at:
                raise ValidationError("The (addendum date) field must be between (start at) and (end at) fields")

    @api.model
    def create(self, vals):
        """
        Override the default create Addendum method
        """
        project_id = vals.get('project_id', False)
        number = vals.get('number', False)
        if project_id and number:
            self._validate_if_number_exists(number=number, project_id=project_id)
        return super(Addendum, self).create(vals)

    def _validate_if_number_exists(self, number, project_id, id=None):
        """
        Validate if the number is repeated by the project selected
        """

        # The domain is the search criterio to filter data

        # el dominio son los criterios que usamos para filtrar informacion
        params = [
            ('project_id', '=', project_id),
            ('number', 'ilike', number)
        ]

        if id is not None:
            params.append(('id', '!=', id))

        counter = self.env['lsv_project.addendum'].search_count(params)
        
        if counter > 0:
            raise ValidationError("The number already exists!.")

    def write(self, vals):
        """
        Override the default write addendum method
        """
        number = vals.get('number', False)
        if number:
            self._validate_if_number_exists(number=number, project_id=self.project_id.id)
        return super(Addendum, self).write(vals)
