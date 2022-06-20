import frappe
import random
def all():
    print("\n\n")
    print("=------------------all")
    new_doc = frappe.get_doc(
        {
            "doctype" : "Note",
            "title" : random.ramdint(0,999)
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
            "title" : random.ramdint(999,999999999)
        }
    )

    new_doc.insert()
    frappe.db.commit()