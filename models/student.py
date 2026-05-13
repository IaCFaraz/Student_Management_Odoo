from odoo import models, fields

class Student(models.Model):
    _name = 'student.student'
    _description = 'Student Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Student Name", required=True, tracking=True)
    father_name = fields.Char(string="Father Name", tracking=True)
    mother_name = fields.Char(string="Mother Name")
    dob = fields.Date(string="Date of Birth")

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string="Gender", tracking=True)

    roll_no = fields.Char(string="Roll No", tracking=True)
    admission_no = fields.Char(string="Admission No")

    # Many2one Course field
    course_id = fields.Many2one('student.course', string="Course", tracking=True)

    # Archived filter ke liye
    active = fields.Boolean(string="Active", default=True)