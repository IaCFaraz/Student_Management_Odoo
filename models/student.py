from odoo import models, fields, api

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

    # Blood Group field
    blood_group = fields.Selection([
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('o+', 'O+'),
        ('o-', 'O-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
    ], string="Blood Group", tracking=True)

    # ============================================
    # METHOD INHERITANCE — create() override
    # ============================================

    @api.model
    def create(self, vals):
        # Step 1: Pehle parent ka create() chalao
        # Isse record database mein save hoga
        record = super(Student, self).create(vals)

        # Step 2: Apna extra kaam karo
        # Naye student ke chatter mein welcome message
        record.message_post(
            body=f"🎉 Welcome! {record.name} has been successfully admitted!",
            message_type='notification',
            subtype_xmlid='mail.mt_note',
        )

        # Step 3: Record return karo
        return record

    # ============================================
    # METHOD INHERITANCE — write() override
    # ============================================

    def write(self, vals):
        # Step 1: Pehle parent ka write() chalao
        result = super(Student, self).write(vals)

        # Step 2: Agar course change hua toh message
        if 'course_id' in vals:
            for record in self:
                record.message_post(
                    body=f"📚 Course has been updated to: {record.course_id.name}",
                    message_type='notification',
                    subtype_xmlid='mail.mt_note',
                )

        # Step 3: Result return karo
        return result