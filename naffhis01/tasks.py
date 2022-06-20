import frappe
def all():
    print("\n\n")
    print("=------------------all")
    new_doc = frappe.get_doc(
        {
            "doctype" : "Note",
            "title" : "Hello world fro all"
        }
    )

    new_doc.insert()
    frappe.db.commit()

def cron():
    print("\n\n")
    print("=------------------Cron")
    new_doc = frappe.get_doc(
        {
            "doctype" : "Note",
            "title" : "Hello world"
        }
    )

    new_doc.insert()
    frappe.db.commit()