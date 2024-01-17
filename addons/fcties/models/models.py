# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Alumne(models.Model):
    _name = 'fcties.alumne'
    _description = 'Alumne'

    name = fields.Char(string="Nombre", required=True, help="Introduce el nombre del alumno")
    surname = fields.Char(string="Apellidos", required=True, help="Introduce los apellidos del alumno")
    date = fields.Date(string="Fecha de nacimiento")
    curso = fields.Selection([("0","20/21"),("1","21/22"),("2","22/23"),("3","23/24")],default="3",string="Curso académico")
    email = fields.Char(string="Email", required=False, help="Introduce el correo electronico")
    tlf = fields.Char(string="Telefono", required=False, help="Introduce el numero de telefono")
    ciclo = fields.Selection([("0","DAM"),("1","DAW"),("2","ASIR")],default="1",string="Ciclo formativo",required=True)
    practicas = fields.Selection([("0","Abril"),("1","Septiembre")],default="0",string="Periodo de prácticas",required=True)
    nota = fields.Float(string="Nota media", required=True)
    nota_text = fields.Text(string="Nota media en texto")
    empresa = fields.Many2one('fcties.empresa', string='Empresa')
    
class Empresa(models.Model):
    _name = 'fcties.empresa'
    _description = 'Empresa'

    name = fields.Char(string="Nombre", required=True, help="Introduce el nombre de la empresa")
    persona = fields.Char(string="Persona de contacto", required=True, help="Introduce la persona de contacto")
    tlf = fields.Char(string="Telefono", required=True, help="Introduce el telefono de contacto")
    email = fields.Char(string="Email", required=True, help="Introduce el correo electronico de contacto")
    direccion = fields.Char(string="Direccion", required=True, help="Introduce la direccion")
    alumnos = fields.One2many('fcties.alumne', 'empresa' ,string='Alumnos')
