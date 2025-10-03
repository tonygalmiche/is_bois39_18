# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProductTemplateAttributeValue(models.Model):
    _inherit = 'product.template.attribute.value'

    color = fields.Integer(
        string="Color",
        compute='_compute_color',
        store=True,
        readonly=False,
        inverse='_inverse_color'
    )

    @api.depends('product_attribute_value_id.color')
    def _compute_color(self):
        for record in self:
            if record.product_attribute_value_id:
                record.color = record.product_attribute_value_id.color
            else:
                record.color = 1

    def _inverse_color(self):
        for record in self:
            if record.product_attribute_value_id:
                record.product_attribute_value_id.color = record.color
