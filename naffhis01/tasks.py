import frappe
def all():
    new_doc = frappe.get_doc(
        {
            "doctype" : "Note",
            "title" : "Hello world fro all"
        }
    )

    new_doc.insert()
    frappe.db.commit()

def cron():
    new_doc = frappe.get_doc(
        {
            "doctype" : "Note",
            "title" : "Hello world"
        }
    )

    new_doc.insert()
    frappe.db.commit()