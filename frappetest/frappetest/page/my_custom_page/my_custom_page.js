frappe.pages['my-custom-page'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		// title: 'custom page',
		single_column: true
	});
	page.set_title('My Page')
	page.set_title_sub('Subtitle')
	page.set_indicator('Pending', 'orange')
	// page.clear_indicator()
	let $btn = page.set_primary_action('New',()=> create_new(), 'octicon octicon-plus' )
	let $btn2 = page.set_secondary_action('Refresh', ()=> refresh(), 'octicon octicon-sunc')
	page.add_menu_item('Send Email', ()=>open_email_dailog(), true)
	page.add_action_item('Delete', ()=> delete_items())
	page.add_inner_button('Update Posts', () => update_posts())
	
	page.add_inner_button('New Post', () => new_post(), 'Make')
	page.remove_inner_button('Update Posts')
	page.change_inner_button_type('Delete Posts', 'Actions', 'danger');
	// page.clear_inner_toolbar()

	let field = page.add_field({
		label: 'Status',
		fieldtype: 'Select',
		fieldname: 'status',
		options: ['Open', 'Closed', 'Cancelled'],
		change: function() {
			console.log(field.get_value()); 
		}
	});
	let  values = page.get_form_values();

}


