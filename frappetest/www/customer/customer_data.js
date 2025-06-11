// frappe.call({
//     method: "frappetest.api.get_customer_data",
//     args : {
//         doctype : "Customer Data",
//         fields : ["emp_name", "emp_role", "emp_salary"]
//     },
//     callback : function(r){
//         if(r.message){
//             console.log(r.message)
//         }
//         else{
//             frappe.msgprint("no data found ")
//         }
//     }
// })