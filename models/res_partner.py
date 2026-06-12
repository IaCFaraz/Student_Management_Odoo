from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_student = fields.Boolean(string="Is Student?")
    student_id = fields.Many2one(
        'student.student',
        string="Linked Student"
    )