# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _

class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = ["res.partner"]

    # Adding a new selection field gender with three options
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('unspecified', 'Unspecified')
    ], string="Gender")
