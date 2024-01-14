# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Escuela(models.Model):
    _name = 'escuela_vela.escuela'
    _description = 'Escuela'

    name = fields.Char(string="Denominacion", required=True, help="Introduce el denominacion de la escuela")
    logo = fields.Image("Logo", max_width=128, max_height=128)
    email = fields.Char(string="Email", required=False, help="Introduce el email de la escuela")
    tlf = fields.Integer(string="Telefono de contacto")
    monitores_ids = fields.One2many('escuela_vela.monitor', 'escuela_id', string='Monitores')


class Curso(models.Model):
    _name = 'escuela_vela.curso'
    _description = 'Curso'

    name = fields.Char(string="Titulo", required=True, help="Introduce el titulo del curso")
    duracion_en_dias = fields.Integer(string='Duración en Días')
    duracion_en_horas = fields.Float(string='Duración en Horas', compute='_compute_duracion_horas', store=True)
    currency_id = fields.Many2one('res.currency', string='Currency')
    price = fields.Monetary(currency_field='currency_id')

    @api.depends('duracion_en_dias')
    def _compute_duracion_horas(self):
        for record in self:
            factor_conversion = 24  # 1 dia = 24 horas
            record.duracion_en_horas = record.duracion_en_dias * factor_conversion


class Monitor(models.Model):
    _name = 'escuela_vela.monitor'
    _description = 'Monitor'

    name = fields.Char(string="Nombre", required=True, help="Introduce el nombre del monitor")
    identification_code = fields.Char(string="Código de Identificación Único", required=True)
    email = fields.Char(string="Email", required=False, help="Introduce el email del monitor")
    tlf = fields.Integer(string="Telefono de contacto")
    escuela_id = fields.Many2one('escuela_vela.escuela', string='Escuela')


class Alumno(models.Model):
    _name = 'escuela_vela.alumno'
    _description = 'Alumno'

    name = fields.Char(string="Nombre", required=True, help="Introduce el nombre del alumno")
    registration_number = fields.Char(string="Número de Matrícula", required=True)
    email = fields.Char(string="Email", required=False, help="Introduce el email del alumno")
    tlf = fields.Integer(string="Telefono de contacto")
    escuela_id = fields.Many2one('escuela_vela.escuela', string='Escuela')
