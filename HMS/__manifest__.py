{

    'name': "hospital",
    'version': '1.0',
    'depends': ['crm'],
    'author': "Author Name",
    'category': 'Category',
    'description': """
    Description text
    """,
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/patient.xml',
        'views/department.xml',
        'views/doctors.xml',
        'views/logs.xml',
        'views/crm_customers.xml',
        "report/hms_patient_template.xml",
        "report/report.xml",
    ],
}