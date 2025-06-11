frappe.pages['vehicle-chart'].on_page_load = function(wrapper) {
    const page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Vehicle Ride Chart',
        single_column: true
    });

    frappe.call({
        method: 'frappetest.frappetest.api.get_vehicle_chart_data',
        callback: function(r) {
            if (r.message) {
                new frappe.Chart( wrapper, {
                    data: {
                        labels: r.message.labels,
                        datasets: r.message.datasets
                    },
                    type: 'bar',
                    height: 300
                });
            }
        }
    });
};
