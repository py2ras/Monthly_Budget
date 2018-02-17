#!/usr/bin/python3
import io
import sys
import unittest
from monthly_budget import MonthlyBudget

class TestMonthlyBudget(unittest.TestCase):
	def setUp(self):
		self.budget_1 = MonthlyBudget("Jan",800,900)
		self.budget_2 = MonthlyBudget("Feb",4000,3000)
		
	def test_get_month(self):
		self.assertEqual(self.budget_1.get_month(), "Jan")
		self.assertEqual(self.budget_2.get_month(), "Feb")
	
		self.budget_1.month = "Mar"
		self.budget_2.month = "Apr"
		
		self.assertEqual(self.budget_1.get_month(), "Mar")
		self.assertEqual(self.budget_2.get_month(), "Apr")

	def test_get_start_amount(self):
		self.assertEqual(self.budget_1.get_start_amount(),800)
		self.assertEqual(self.budget_2.get_start_amount(), 4000)
	
	def test_add_show_expenses(self):
		self.budget_1.add_expenses(travel=400,education=500,games=300,entertainment=1000)
		self.budget_2.add_expenses(travel=800,education=900,games=700,entertainment=3000)
		
		# source -https://stackoverflow.com/a/34738440/9285808 
		capturedOutput = io.StringIO()				# Create StringIO object
		sys.stdout = capturedOutput				# Redirect stdout
		
		self.budget_1.show_expenses()				# Call function
		self.budget_2.show_expenses()				# Call function	
		
		sys.stdout = sys.__stdout__				# Reset redirect
		print("Captured output:\n", capturedOutput.getvalue())
		
	def test_add_show_income(self):
		self.budget_1.add_income(paycheck=700,loan=1500,stock=200)
		self.budget_2.add_income(paycheck=1700,loan=3500,stock=2000)

		# source - https://stackoverflow.com/a/34738440/9285808
		capturedOutput = io.StringIO()				# Create StringIO object
		sys.stdout = capturedOutput				# Redirect stdout
		
		self.budget_1.show_income()				# Call function
		self.budget_2.show_income()				# Call function	
		
		sys.stdout = sys.__stdout__				# Reset redirect
		print("Captured output:\n", capturedOutput.getvalue())

	def test_get_total_expenditure(self):
		self.budget_1.expenses = {'travel':400,'education':500,'games':300,'entertainment':1000}
		self.budget_2.expenses = {'travel':800,'education':900,'games':700,'entertainment':3000}
		self.assertEqual(self.budget_1.get_total_expenditure(),2200)
		self.assertEqual(self.budget_2.get_total_expenditure(),5400)

	def test_get_total_income(self):
		self.budget_1.income = {'paycheck':700,'loan':1500,'stock':200}
		self.budget_2.income = {'paycheck':1700,'loan':3500,'stock':2000}
		self.assertEqual(self.budget_1.get_total_income(),3200)
		self.assertEqual(self.budget_2.get_total_income(),11200)


	def test_get_excess_expense(self):
		self.budget_1.expenses = {'travel':400,'education':500,'games':300,'entertainment':1000}
		self.budget_2.expenses = {'travel':800,'education':900,'games':700,'entertainment':3000}
		self.assertEqual(abs(self.budget_1.get_excess_expense()), 1300)
		self.assertEqual(abs(self.budget_2.get_excess_expense()), 2400)
	
	def test_get_total_difference(self):
		self.budget_1.expenses = {'travel':400,'education':500,'games':300,'entertainment':1000}
		self.budget_2.expenses = {'travel':800,'education':900,'games':700,'entertainment':3000}
		self.budget_1.income = {'paycheck':700,'loan':1500,'stock':200}
		self.budget_2.income = {'paycheck':1700,'loan':3500,'stock':2000}
		self.assertEqual(self.budget_1.get_total_difference(), 1000)
		self.assertEqual(self.budget_2.get_total_difference(), 5800)
	
	def tearDown(self):
		print("Done!")

if __name__ == '__main__':
	unittest.main()


