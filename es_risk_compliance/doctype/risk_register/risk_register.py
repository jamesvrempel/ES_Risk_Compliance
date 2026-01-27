# Copyright (c) 2024, ES Australia and contributors
# For license information, please see license.txt

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
			likelihood = int(self.likelihood_score.split(' - ')[0])
			impact = int(self.impact_score.split(' - ')[0])
			score = likelihood * impact
			
			self.inherent_risk_rating = self.get_risk_rating(score)
	
	def calculate_residual_risk(self):
		"""Calculate residual risk rating after controls"""
		if self.residual_likelihood and self.residual_impact:
			likelihood = int(self.residual_likelihood.split(' - ')[0])
			impact = int(self.residual_impact.split(' - ')[0])
			score = likelihood * impact
			
			self.residual_risk_rating = self.get_risk_rating(score)
	
	def get_risk_rating(self, score):
		"""Convert numeric score to risk rating"""
		if score >= 15:
			return "Critical ({})" .format(score)
		elif score >= 10:
			return "High ({})".format(score)
		elif score >= 5:
			return "Medium ({})".format(score)
		else:
			return "Low ({})".format(score)
	
	def on_submit(self):
		"""Update last review date on submission"""
		self.db_set('last_review_date', frappe.utils.today())
		
	def before_update_after_submit(self):
		"""Recalculate risk ratings on update"""
		self.calculate_inherent_risk()
		self.calculate_residual_risk()
