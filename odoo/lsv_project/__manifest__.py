{
	'name': "MyFirtModule",
	'version': "2.1-devl6",
	'summary': "This is my firt module, make in odoo, I'm happy (Y)",
	'depends': ['project', 'contacts'],
	'data': {
		'security/module_groups.xml',
		'security/ir.model.access.csv',
		'data/addendum_description_data.xml',
	},
	'installable': True,
	'auto_install': False,
	'license': "LGPL-3",

}
