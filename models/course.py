from odoo import models, fields

class Course(models.Model):
    _name = 'student.course'
    _description = 'Course'

    name = fields.Char(string="Course Name", required=True)
    code = fields.Char(string="Course Code")
    description = fields.Text(string="Description")
    student_ids = fields.One2many('student.student', 'course_id', string="Students")