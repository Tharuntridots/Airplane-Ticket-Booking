frappe.ui.form.on('TestImport', {
    refresh: function(frm) {
        frappe.call({
            method: 'frappetest.frappetest.doctype.testimport.testimport.get_driver_chart_data',
            callback: function(r) {
                if (r.message) {
                    const chart_data = r.message;
                    
                    // Prepare chart options for frappe chart
                    let chart = new frappe.Chart( 
                        // Bind the chart to the HTML field's div
                        frm.fields_dict.chart_html.$wrapper[0], 
                        {
                            data: chart_data.data,
                            type: chart_data.type,
                            height: chart_data.height,
                            colors: chart_data.colors,
                            title: chart_data.title
                        }
                    );
                }
            }
        });
    }
});



