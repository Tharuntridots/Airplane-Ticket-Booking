frappe.pages['testimport'].on_page_load = function(wrapper) {
    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Driver Chart',
        single_column: true
    });

    // Add a div where the chart will be rendered
    $(wrapper).find('.layout-main-section').append('<div id="chart" style="margin-top:30px;"></div>');

    // Call server to get data
    frappe.call({
        method: 'frappetest.testimport.testimport.get_driver_chart_data',
        callback: function(r) {
            const data = r.message;

            const chart = new frappe.Chart("#chart", {
                title: "Driver Registrations",
                data: data,
                type: 'bar',
                height: 300,
                colors: ['#21ba45']
            });
        }
    });
};
