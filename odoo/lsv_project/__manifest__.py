{
	'name': "MyFirtModule",
	'version': "2.1-devl16",
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
		'view/res_config_settings_view.xml',
		'view/res_partner_view.xml',
		'view/project_project_view.xml',
	},
	'installable': True,
	'auto_install': False,
	'license': "LGPL-3",

}
