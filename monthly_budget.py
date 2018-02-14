#!/usr/bin/python3

# Program to set and manage monthly budget
# @author - Sarthak Sharma <sarthak.gatech@gmail.com>
# Date of Last Modification - 02/14/2018

import sys

class MonthlyBudget:
	
	def __init__(self, month, startAmount, expectedExpenditure):
		self.month = month
		self.startAmount = startAmount
		self.expectedExpenditure = expectedExpenditure
	
	def setStartAmount(self,newStartAmount):
		self.startAmount = newStartAmount

	def getStartAmount(self):
		return self.startAmount
	

jan_budget = MonthlyBudget('January',700,600)

print(jan_budget.month)	
print(jan_budget.getStartAmount())
jan_budget.setStartAmount(900)
print(jan_budget.getStartAmount())
