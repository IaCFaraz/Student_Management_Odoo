# -*- coding: utf-8 -*-
{
    'name': 'Student Management',
    'version': '1.0',
    'summary': 'Manage student records',
    'description': 'Module to manage students (name, age, course)',
    'author': 'Faraz',
    'website': 'https://www.devsecure.com',
    'category': 'Education',
    'depends': ['base', 'web', 'mail', 'contacts'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/course_views.xml',
        'views/student_views.xml',
        'views/student_views_inherit.xml',
        'views/attendance_views.xml',
        'views/student_partner_views.xml',
        'reports/student_report.xml',
    ],
    'installable': True,
    'application': True,
}