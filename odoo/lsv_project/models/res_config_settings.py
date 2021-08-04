# -*- conding: utf-8 -*-
"""
All models from the res config setting
"""
from odoo import models, fields

class ResConfigSetting(models.TransientModel):
    _inherit = 'res.config.settings'
    google_maps_api_key = fields.Char(string='Google map api key')