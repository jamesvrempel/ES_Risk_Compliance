# -*- coding: utf-8 -*-
# Copyright (c) 2026, ES Australia and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class RiskRegister(Document):
	def validate(self):
		"""Calculate risk ratings before saving"""
		self.calculate_inherent_risk()
		self.calculate_residual_risk()
	
	def calculate_inherent_risk(self):
		"""Calculate inherent risk rating from likelihood and impact"""
		if self.likelihood_score and self.impact_score:
			likelihood = int(self.likelihood_score[0])  # Get first character (1-5)
			impact = int(self.impact_score[0])  # Get first character (1-5)
			rating = likelihood * impact
			
			# Determine risk level
			if rating >= 20:
				self.inherent_risk_rating = "Critical"
			elif rating >= 12:
				self.inherent_risk_rating = "High"
			elif rating >= 6:
				self.inherent_risk_rating = "Medium"
			else:
				self.inherent_risk_rating = "Low"
	
	def calculate_residual_risk(self):
		"""Calculate residual risk rating from residual likelihood and impact"""
		if self.residual_likelihood and self.residual_impact:
			likelihood = int(self.residual_likelihood[0])  # Get first character (1-5)
			impact = int(self.residual_impact[0])  # Get first character (1-5)
			rating = likelihood * impact
			
			# Determine risk level
			if rating >= 20:
				self.residual_risk_rating = "Critical"
			elif rating >= 12:
				self.residual_risk_rating = "High"
			elif rating >= 6:
				self.residual_risk_rating = "Medium"
			else:
				self.residual_risk_rating = "Low"
	
	def on_submit(self):
		"""Actions when risk is submitted"""
		self.db_set('last_review_date', frappe.utils.today())
