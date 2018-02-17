#!/usr/bin/python3

# Program to set and manage monthly budget
# [TO DO]: Add ML algorithms to analyse expenditure and investment patterns
# @author - Sarthak Sharma <sarthak.gatech@gmail.com>
# Date of Last Modification - 02/14/2018

import sys

class MonthlyBudget:
	
	def __init__(self, month, startAmount, expectedExpenditure):
		self.month = month
		self.startAmount = startAmount
		self.expectedExpenditure = expectedExpenditure
		self.expenses = {}
		self.income = {}
	
	def get_month(self):
		return str(self.month)

	def get_start_amount(self):
		return self.startAmount
	
	def add_expenses(self, **kwargs):
		for itemKey in kwargs:
			expense = int(kwargs[itemKey])
			self.expenses[str(itemKey)] = expense

	def add_income(self, **kwargs):
		for incomeSource in kwargs:
			incomeAmount = int(kwargs[incomeSource])
			self.income[str(incomeSource)] = incomeAmount
	
	def show_income(self):
		# [TO DO]: Enhance the printing later
		print("Your income for the month ", self.month," is:\nSource\t\t\t\tAmount")
		for incomeSource,incomeAmount in self.income.items():
			print(incomeSource, "\t\t\t\t", incomeAmount)			

	def show_expenses(self):
		# [TO DO]: Enhance the printing later
		print("Your expenditure for the month ", self.month," is:\nItem\t\t\t\tCost")
		for itemKey,costValue in self.expenses.items():
			print(itemKey, "\t\t\t\t", costValue)			
	
	def get_total_expenditure(self):
		return sum([v for k,v in self.expenses.items()])

	def get_total_income(self):
		return sum([v for k,v in self.income.items()]) + self.startAmount

	def get_excess_expense(self):
		totalExpenditure = self.get_total_expenditure()
		excessExpense = self.expectedExpenditure - totalExpenditure
		return excessExpense 

	def get_total_difference(self):
		totalIncome = self.get_total_income()
		totalExpenditure = self.get_total_expenditure()
		totalDifference = totalIncome - totalExpenditure
		return totalDifference	

#jan_budget = MonthlyBudget('January',700,600)
#jan_budget.add_expenses(food=300)
#jan_budget.add_expenses(travel=400,education=500,games=300,entertainment=1000)
#jan_budget.add_expenses(Misc=400)
#jan_budget.show_expenses()
#print(jan_budget.get_total_expenditure())
#
#
