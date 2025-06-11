// Copyright (c) 2025, tharun and contributors
// For license information, please see license.txt




// frappe.ui.form.on('Patient Record', {
//     validate: function(frm) {
//         if (frm.doc.age < 18) {
//             frappe.msgprint("The patient is under 18");
//         }
//     },

//     gender: function(frm) {
//         if (frm.doc.gender === 'other') {
//             frappe.msgprint("Please confirm gender manually");
//         }
//         gender_save_button(frm)
//     }
// });

// frappe.ui.form.on('Prescription', {
//     medicine_name: function(frm, cdt, cdn) {
//         let row = locals[cdt][cdn];
//         if (row.medicine_name === "Paracetamol") {
//             row.dosage = "500mg";
//             frm.refresh_field("prescriptions");
//         }
//     }
// });

// frappe.ui.form.on('Patient Record', {
//     refresh: function(frm) {
//         if (!frm.doc.__on_refresh_save_done) {  // custom flag check
//             // frappe.msgprint("This is a test message");
//             frm.set_value('age', '30');
//             frm.refresh_field('age')
//             frm.doc.__on_refresh_save_done = true;  // set the flag
//             // frm.save('Submit');
//         }
//     }
// });


// frappe.ui.form.on('Prescription', {
//     prescription_add : function(frm, cdt, cdn){
//         frappe.msgprint("The new prescription is added")
//     }
// })

// function gender_save_button(frm){
//     if(frm.doc.gender === 'Female'){
//         frm.enable_save();
//     }else{
//         frm.disable_save()
//     }
// }

// frappe.ui.form.on('Patient Record', {
    // after_save : function(frm){
    //     frappe.msgprint("Refresh with latest values");
    //     frm.reload_doc();
    // },

    // onload: function(frm) {
    //     if (!frm.doc.patient_name) {
    //         frappe.msgprint("Patient name is missing", "orange");
    //     }

    //     // Add browser data and set form as dirty (unsaved)
    //     frm.doc.browser_data = navigator.userAgent;
    //     frm.dirty();
    // },

    // refresh: function(frm) {
    //     // Add email button
    //     frm.add_custom_button('Email Patient Record', () => {
    //         frm.email_doc(`Hello ${frm.doc.patient_name},\n\nPlease find your prescription attached.`);
    //     });

    //     // Add "Click Me" button only if form is not new
    //     if (!frm.is_new()) {
    //         frm.add_custom_button('Click Me', () => {
    //             console.log('Custom button clicked');
    //         });
    //     }

    //     frm.change_custom_button_type('Click Me', null, 'danger');

    //     setTimeout(()=>{
    //         frm.remove_custom_button('Click Me')
    //     }, 2000);

    //     setTimeout(()=>{
    //         frm.clear_custom_buttons();
    //         frappe.msgprint("All custom buttons removed");
    //     }, 3000)

    //     // Alert if the form has unsaved changes
    //     if (frm.is_dirty()) {
    //         frappe.show_alert('You have unsaved changes');
    //     }
    // },

    // gender : function (frm){
    //     if (frm.doc.gender === 'Other'){
    //         frm.set_df_property('age', 'fieldtype', 'Text');
    //         frm.refresh_field('age')
            
    //     } else{
    //         frm.set_df_property('age', 'fieldtype', 'Data');
    //         frm.refresh_field('age')
    //     }
    // },

    // gender : function(frm){
    //     if(frm.doc.gender === 'Other'){
    //         frm.toggle_enable('age', false)
    //     }
    //     else {
    //         frm.toggle_enable('age', true)
    //     }
    // },

    // setup: function(frm) {
    //     frm.set_query('medicine_name', 'prescription', function(doc, cdt, cdn)  {
    //         return {
    //             filters: {
    //                 is_active: 1, // Example filter if your "Medicine" Doctype has an `is_active` checkbox
    //             }
    //         };
    //     });
    // },

// })


// frappe.ui.form.on('Patient Record', {
//     refresh : function(frm){
//         if(!frm.custom_next_visit){
//             let wrapper = frm.fields_dict.prescription.wrapper;

//             let $div = $('<div class="next-visit-wrapper" style="margin-top: 15px;"></div>').appendTo(wrapper);

//             frm.custon_next_visit = frappe.ui.form.make_control({
//                 parent : $div,
//                 df: {
//                     label : 'Next Visit Date', 
//                     fieldname: 'next_visit_date',
//                     fieldtype : 'Date',
//                     reqd: 0
//                 },
//                 render_input : true 
//             });
//         }
//     }
// })


// frappe.ui.form.on("Patient Record", {
//     onload(frm){
//         frappe.meta.docfield_map["Patient Record"]["gender"].formatter = ()=> {
//             if (value === "Male") return " 🚹 Male"
//             if (value === "Female") return " 🚺 Male"
//             return value
//         }
//     }
// })

// frappe.listview_settings['Patient Record'] = {
//     add_fields: ['patient_name', 'age', 'gender'],

//     filters: [
//         ['gender', '=', 'Male']
//     ],

    // hide_name_column: true,

    // get_indicator(doc) {
    //     if (doc.age && parseInt(doc.age) < 18) {
    //         return ['Child', 'blue', 'age,<,18'];
    //     } else {
    //         return ['Adult', 'green', 'age,>=,18'];
    //     }
    // },

    // button: {
    //     show(doc) {
    //         return !!doc.patient_name;
    //     },
    //     get_label() {
    //         return 'View Profile';
    //     },
    //     action(doc) {
    //         frappe.set_route('Form', 'Patient Record', doc.name);
    //     }
    // },

    // formatters: {
    //     patient_name(val) {
    //         return `<b>${val}</b>`;
    //     },
    //     gender(val) {
    //         return val === 'Male' ? '👦 Male' : val === 'Female' ? '👧 Female' : val;
    //     }
    // }
// };


// frappe.listview_settings['Patient Record'] = {

    // add_fields :  ['Patient_name', "age", "gender"],

    // filter: [
    //     ['gender', '=', 'Female']
    // ], 

    // hide_name_column: true,

    //  get_indicator(doc) {
    //     if (doc.age && parseInt(doc.age) < 18) {
    //         return ['Child', 'blue', 'age,<,18'];
    //     } else {
    //         return ['Adult', 'green', 'age,>=,18'];
    //     }
    // },

    // button: {
    //     show(doc) {
    //         return !!doc.patient_name;
    //     },
    //     get_label() {
    //         return 'View Profile';
    //     },
    //     action(doc) {
    //         frappe.set_route('Form', 'Patient Record', doc.name);
    //     }
    // },

    // formatters: {
    //     patient_name(val){
    //         return `<b>${val}</b>`
    //     },
    //     gender(val){
    //         return  val === 'Male' ? '👦 Male' : val === 'Female' ? '👧 Female' : val;
    //     }
    // },

// }

    // console.log(frappe.get_route());


    // frappe.set_route('Form', 'Patient Record', 'PAT-0015');
    // frappe.set_route(['List', 'Patient Records', 'List'], { gender: 'Female' });

    // frappe.format('2019-09-08', { fieldtype: 'Date' })


// frappe.ui.form.on('Patient Record', {
//     refresh(frm){
//         frm.add_custom_button('Quick Add', () => {
//             let d = new frappe.ui.Dialog({
//                 title : "add patient",
//                 fields: [
//                     {label: 'Patient Name', 'fieldname': 'patient_name', fieldtype: 'Data'}
//                 ], 
//                 primary_action_label: 'Save',
//                 primary_action(values){
//                     frappe.call({
//                         method: 'frappe.client.insert',
//                         args:{
//                             doc:{
//                                 doctype: 'Patient Record', 
//                                 patient_name: values.patient_name
//                             }
//                         },
//                         callback: (r) => {
//                             frappe.throw('Patient $(r.message.name) created');
//                             d.hide();
//                         }
//                     })
//                 }
//             })
//             d.show();
//         });
//     }
// });

// frappe.ui.form.on('Patient Record', {
//     refresh(frm) {
//         // frappe.prompt([
//         //     {
//         //         label: 'First Name',
//         //         fieldname : 'first_name',
//         //         fieldtype: 'Data'
//         //     }
//         // ],(values)=>{
//         //     console.log(values.first_name)
//         // })

//         // frappe.show_alert('Hi, you mave new message', 5)
//         // frappe.show_alert({
//         //     message: __('Hi, you mave new message', 5),
//         //     indicator : 'green'
//         // }, 5)
//         frappe.ui.update_chart(2, [30]);        
//     }
// });

//whitelist function?
// frappe.ui.form.on('Patient Record', {
//     refresh(frm) {
//         frappe.call({
//             method: 'frappetest.frappetest.doctype.patient_record.patient_record.get_patient_details',
//             args : {
//                 patient_name:'john'
//             }, 
//             callback: function(response){
//                 frappe.msgprint("Patient data:"+ JSON.stringify(response.message));
//             }
//         })    
//     }
// });


// frappe.ui.form.on('Patient Record', {
//     refresh(frm) {
        // frappe.db.get_doc('Patient Record', 'PAT-0030')
        // .then(docc =>{
        //     console.log(docc)
        // }), 
        // frappe.db.get_value('Patient Record', 'PAT-0030', 'age')
        // .then(docc =>{
        //     // console.log(docc.message.age)
        //     frappe.msgprint("age: " + JSON.stringify(docc.message.age))
        // })

        // frappe.db.get_list('Patient Record', {
        //    fields: ['name', 'patient_name', 'age'],
        //    filters : [
        //     ['age', '>', '30']
        //    ]
        // }).then(records => {
        //     console.log(records)
        // })

        // frappe.db.set_value('Patient Record', 'PAT-0031', 'age', '48')
        // .then(r=>{
        //     let doc = r.message;
        //     console.log(doc);
        //     frappe.msgprint(doc.name)
        // })

        // frappe.db.insert({
        //     doctype : 'Patient Record',
        //     patient_name : "alice",
        //     age: '34',
        //     gender : 'Female'
        // }).then(doc =>{
        //     console.log("inserted", doc)
        // })

        // frappe.db.count('Patient Record')
        //     .then(count => {
        //         console.log("Total Patient Records:", count);
        //     });

        // frappe.db.delete_doc('Patient Record', 'PAT-0027')
        // .then(r => {
        //     console.log("deleted")
        // })

        // frappe.db.exists('Patient Record', 'PAT-0019')
        //     .then(exists => {
        //         if (exists) {
        //             console.log("Patient PAT-0019 exists.");
        //         } else {
        //             console.log("Patient PAT-0001 does not exist.");
        //         }
        //     });


//     }
// });

// frappe.ui.form.on('Patient Record', {
    
    
// });


// let cr= frappe.get_route();
// console.log(cr)

    // frappe.set_route('Form', 'Patient Record', 'PAT-0015');
    // frappe.set_route(['List', 'Patient Record', 'List'], {
    //     gender: 'Female'
    // });


// ---------------------------------------------------------------------------------------------------------------------------------------------------
// ---------------------------------------------------------------------------------------------------------------------------------------------------


//Advance Js


// frappe.ui.form.on('Patient Record', {
//     onload(frm) {
//         // Find the chart field wrapper
//         let wrapper = frm.fields_dict.chart.wrapper;

//         // Add chart container
//         $(wrapper).html(`<div id="live_chart" style="height: 250px;"></div>`);

//         // Initial empty chart data
//         const data = {
//             datasets: [{
//                 name: "Patient Age Data",
//                 values: []
//             }]
//         };

//         // Initialize the RealtimeChart
//         frm.chart = new frappe.ui.RealtimeChart("#live_chart", "test_event", 10, {
//             title: "Patient Age Chart",
//             data: data,
//             type: "bar", 
//             height: 200,
//             colors: ["#28a745"]
//         });

//         // Start updating
//         frm.chart.start_updating();
//     },

//     on_unload(frm) {
//         if (frm.chart) {
//             frm.chart.stop_updating();
//         }
//     }
// });


//scanner api camera not present 
// frappe.ui.form.on('Patient Record', {
//   refresh(frm) {
//     frm.add_custom_button('Scan Barcode', () => {
//       const scanner = new frappe.ui.Scanner({
//         dialog: true,
//         multiple: false,
//         on_scan(data) {
//             console.log('Scanned:', data.decodedText);
//             // Optionally close the scanner manually here
//             scanner.stop_scan();
//         }
//         });

//         // Open scanner dialog explicitly
//         scanner.show_dialog();

//     });
//   }
// });

// frappe.call({
//     method: "frappetest.frappetest.doctype.patient_record.patient_record.get_patient_record", 
//     args: {
//         docname: "PAT-0025"
//     },
//     callback: function(r) {
//         console.log(r.message);
//     }
// });


frappe.call({
    method: "frappetest.frappetest.doctype.patient_record.patient_record.change_age",
    // args: {
    //     docname: "PAT-0027",
    //     // fieldname: "age",
    //     // value: 99
    // },
    callback: function(r) {
        if (r.message) {
            console.log("Updated:", r.message);
        } else {
            frappe.msgprint("No response received.");
        }
    }
});


