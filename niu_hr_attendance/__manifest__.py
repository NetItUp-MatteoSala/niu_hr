{
    'name': 'NIU HR Attendance report',
    'version': '0.0',
    'category': 'Human Resources/Attendances',
    'summary': 'Qweb report to track hours worked',
    'description': """
This module aims to track employee's work hours and output them in a human readable format.
       """,
    'website': 'https://www.netitup.it',
    'depends': ['hr', 'hr_attendance', 'base'],
    'data': [
        #'security/ir.model.access.csv',
        'reports/hr_attendance_report_templates.xml',
        'reports/hr_attendance_views.xml',
        'reports/external_layout.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}