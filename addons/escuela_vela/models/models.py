# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Escuela(models.Model):
    _name = 'escuela_vela.escuela'
    _description = 'Escuela'

    name = fields.Char(string="Denominacion", required=True, help="Introduce el denominacion de la escuela")
    logo = fields.Binary("logo")
    email = fields.Char(string="Email", required=False, help="Introduce la direccion de email")
    tlf = fields.Char(string="Telefono", required=False, help="Introduce el numero de telefono")
    monitores_ids = fields.One2many('escuela_vela.monitor', 'escuela_id', string='Monitores')


class Curso(models.Model):
    _name = 'escuela_vela.curso'
    _description = 'Curso'

    name = fields.Char(string="Titulo", required=True, help="Introduce el titulo del curso")
    duracion_en_dias = fields.Integer(string='Duración en Días')
    duracion_en_horas = fields.Float(string='Duración en Horas', compute='_compute_duracion_horas', store=True)
    currency_id = fields.Many2one('res.currency', string='Moneda')
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
    identification_code = fields.Char(string="Identificación", required=True)
    email = fields.Char(string="Email", required=False, help="Introduce el email del monitor")
    tlf = fields.Char(string="Telefono", required=False, help="Introduce el numero de telefono")
    escuela_id = fields.Many2one('escuela_vela.escuela', string='Escuela')


class Alumno(models.Model):
    _name = 'escuela_vela.alumno'
    _description = 'Alumno'

    name = fields.Char(string="Nombre", required=True, help="Introduce el nombre del alumno")
    registration_number = fields.Char(string="Número de Matrícula", required=True)
    email = fields.Char(string="Email", required=False, help="Introduce el email del alumno")
    tlf = fields.Char(string="Telefono", required=False, help="Introduce el numero de telefono")
    escuela_id = fields.Many2one('escuela_vela.escuela', string='Escuela')
