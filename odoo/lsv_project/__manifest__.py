{
	'name': "MyFirtModule",
	'version': "2.1-devl14",
	'summary': "This is my firt module, make in odoo, I'm happy (Y)",
	'depends': ['project', 'contacts'],
	'data': {
		'security/module_groups.xml',
		'data/addendum_description_data.xml',
		'data/policy_type_data.xml',
		'data/endorsement_reason_data.xml',
		'data/resident_role_data.xml',
		'security/ir.model.access.csv',
		'view/addendum_description_view.xml',
		'view/module_menuitems.xml',
	},
	'installable': True,
	'auto_install': False,
	'license': "LGPL-3",

}
