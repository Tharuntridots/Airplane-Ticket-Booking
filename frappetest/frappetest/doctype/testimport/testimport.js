// Copyright (c) 2025, tharun and contributors
// For license information, please see license.txt

// frappe.ui.form.on("TestImport", {
// 	refresh(frm) {

// 	},
// });


// frappe.call({
//     method: "frappetest.frappetest.doctype.testimport.testimport.get_driver_details",
//     args:{
//         driverid : 12
//     },
//     callback: function(r){
//         if(r.message){
//             frappe.msgprint(`Driver Name : ${r.message.firstname} ${r.message.lastname}`)
//         }
//     }

// })

// frappe.ui.form.on('TestImport', {
//   refresh: function(frm) {
//     frappe.call({
//       method: "frappetest.frappetest.doctype.testimport.testimport.get_driver_chart_data",
//       callback: function(r) {
//         if (r.message) {
//           frm.dashboard.add_chart({
//             title: "Drivers Created Per Month",
//             data: r.message,
//             type: 'line'  // or bar, pie
//           });
//         }
//       }
//     });
//   }
// });



