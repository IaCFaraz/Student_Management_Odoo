from odoo import models, fields, api

class StudentAttendance(models.Model):
    _name = 'student.attendance'
    _description = 'Student Attendance'
    _inherit = ['mail.thread']

    name = fields.Char(string="Reference", compute='_compute_name', store=True)
    student_id = fields.Many2one('student.student', string="Student", required=True, tracking=True)
    course_id = fields.Many2one('student.course', string="Course", related='student_id.course_id', store=True)
    date = fields.Date(string="Date", required=True, default=fields.Date.today, tracking=True)
    status = fields.Selection([
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
    ], string="Status", required=True, default='present', tracking=True)
    notes = fields.Text(string="Notes")

    @api.depends('student_id', 'date')
    def _compute_name(self):
        for rec in self:
            if rec.student_id and rec.date:
                rec.name = f"{rec.student_id.name} - {rec.date}"
            else:
                rec.name = "New Attendance"