# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class DynamicRecipients(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		docfield_reference: DF.Literal[None]
		email_field: DF.Literal[None]
		filter_value: DF.Data | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		target_doctype: DF.Link | None
		target_field: DF.Literal[None]
	# end: auto-generated types

	pass
