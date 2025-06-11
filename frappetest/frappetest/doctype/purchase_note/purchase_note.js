frappe.realtime.on("purchase_note_created", function (data) {
    console.log("📢 Realtime Event Triggered!");
    console.log("Note Name:", data.note_name);
    console.log("Amount:", data.amount);
    console.log("Status:", data.status);
});
