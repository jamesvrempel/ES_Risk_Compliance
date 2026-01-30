# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Risk Management"),
			"items": [
				{
					"type": "doctype",
					"name": "Risk Register",
					"label": _("Risk Register"),
					"description": _("Manage organizational risks")
				},
				{
					"type": "doctype",
					"name": "Risk Category",
					"label": _("Risk Categories"),
					"description": _("Categorize risks")
				}
			]
		}
	]
