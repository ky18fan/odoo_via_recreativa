# -*- coding: utf-8 -*-
# Copyright © Via Recreactiva - All Rights Reserved
# Author      Christian Daniel Medina Herrera

from odoo import api, fields, models, _


class ReporteAccidentes(models.Model):
    _name = 'reporte.accidentes'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Reporte de Accidentes'

    name = fields.Char(
        string=_('Folio de reporte'),
        required=True,
        copy=False,
        # readonly=True,
        index=True
    )

    fecha = fields.Date(
        string='Fecha',
        # required=True
    )

    jornada = fields.Char(
        string='Jornada',
        # required=True
    )

    tramo = fields.Char(
        string='Tramo',
        # required=True
    )

    @api.model
    def create(self, vals):
        print('test')
        result = super(ReporteAccidentes, self).create(vals)
        result['name'] = self.env['ir.sequence'].next_by_code('reporte.accidentes') or _('New')
        return result
