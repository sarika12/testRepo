''' this will give the month and day reamaning in your birthday''' 

import sys
import time
def is_leap(year):
	if year % 4 == 0:
		if (year % 100 == 0 and year % 400 == 0):		
			return True
		elif(year % 100 == 0 and year % 400 != 0):
			return False
		else:
			return True
	else:
			return False

def birthday():
	date = time.strftime("%d/%m/%Y")
	birthday_date = raw_input('Enter birthday date in day/month/year==>')
	list1 = birthday_date.split('/')
	list2 = date.split('/')
	list1[2] = list2[2]
	b_day = int(list2[0])
	b_month =int(list2[1])
	b_year = int(list2[2])

	c_day = int(list1[0])
	c_month =int(list1[1])
	c_year = int(list1[2])
  	

	
	if (c_day > b_day) and (c_month == b_month):
		day = c_day - b_day
		month = c_month - b_month
		year = c_year - b_year
		print 'your birthday after',month,'Month','and',day,'days'



	'''elif (c_day > b_day) and (c_month > b_month):
		day = c_day - b_day
		month = c_month - b_month
		print 'your birthday after',month,'Month','and',day,'days'
	
	elif (c_day > b_day) and (c_month < b_month):
		day = c_day - b_day
		month = c_month + 12 - b_month
		print 'your birthday after',month,'Month','and',day,'days'
	
	elif(c_day <= b_day) and (c_month <= b_month):
		if is_leap(c_year) and b_month == 2:
			c_month += 11
			b_day = 29 - bday
			day = c_day + b_day
			month = c_month - b_month
			print 'your birthday after',month,'Month','and',day-1,'days'
	
		elif b_month == 2:
			c_month += 11 
			b_day = 28 - b_day
			day = c_day + b_day
			month = c_month - b_month
			print 'your birthday after',month,'Month','and',day-1,'days'
			
	
		else:
			list1 = [1, 3, 5, 7, 8 ,10,12]
			if(b_month in list1):
				c_month += 11 
				b_day = 31 - b_day
				day = c_day + b_day
				month = c_month - b_month
				print 'your birthday after',month,'Month','and',day-1,'days'
			else:
				c_month += 11 
				b_day = 30 - b_day
				day = c_day + b_day
				month = c_month - b_month
				print 'your birthday after',month,'Month','and',day-1,'days'''
	else:
		list1 = [1, 3, 5, 7, 8 ,10,12]
		if is_leap(b_year) and b_month == 2:
			b_day = 29- b_day
			day = c_day + b_day
			month = c_month - b_month
			print 'your birthday after',month-1,'Month','and',day-1,'days'
	
		elif b_month == 2:
			b_day = 28 - b_day
			day = c_day + b_day
			month = c_month - b_month
			year = c_year - b_year
			print 'your birthday is',month-1,'Month','and',day-1,'days'
			
			
		elif(b_month in list1):
			b_day = 31 - b_day
			day = c_day + b_day
			month = c_month - b_month
			print 'your birthday after',month-1,'Month','and',day-1,'days'
		else:
			b_day = 30 -b_day
			day = c_day + b_day
			month = c_month - b_month
			print 'your birthday after',month-1,'Month','and',day-1,'days'

if __name__ == '__main__':
	birthday()
