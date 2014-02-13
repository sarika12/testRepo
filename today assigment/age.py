'''it will give to you your current age in year month and days'''

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
	c_day = int(list2[0])
	c_month =int(list2[1])
	c_year = int(list2[2])

	b_day = int(list1[0])
	b_month =int(list1[1])
	b_year = int(list1[2])
  	

	

	if (c_day == b_day) and (c_month == b_month):
		day = c_day - b_day
		month = c_month - b_month
		year = c_year - b_year
		print 'you are',year,'year',month,'Month','and',day,'days'
	elif (c_day == b_day) and (c_month < b_month):
		c_year -= 1
		c_month += 12
		day = c_day - b_day
		month = c_month - b_month
		year = c_year - b_year
		print 'you are',year,'year',month,'Month','and',day,'days'


	elif (c_day > b_day) and (c_month > b_month):
		day = c_day - b_day
		month = c_month - b_month
		year = c_year - b_year
		print 'you are',year,'year',month,'Month','and',day,'days'
	
	elif (c_day > b_day) and (c_month < b_month):
		c_year -= 1
		c_month += 12
		day = c_day - b_day
		month = c_month - b_month
		year = c_year - b_year
		print 'you are',year,'year',month,'Month','and',day,'days'
	
	elif(c_day <= b_day) and (c_month <= b_month):
		if is_leap(c_year) and c_month == 2:
			c_year -= 1
			c_month += 12 
			c_month -= 1
			c_day += 29
			day = c_day - b_day
			month = c_month - b_month
			year = c_year - b_year
			print 'you are',year,'year',month,'Month','and',day,'days'
	
		elif c_month == 2:
			c_year -= 1
			c_month += 12 
			c_month -= 1
			c_day += 28
			day = c_day - b_day
			month = c_month - b_month
			year = c_year - b_year
			print 'you are',year,'year',month,'Month','and',day,'days'
			
	
		else:
			list1 = [1, 3, 5, 7, 8 ,10,12]
			if(c_month in list1):
				c_year -= 1
				c_monthperticuler += 12 
 				c_month -= 1
				c_day += 31
				day = c_day - b_day
				month = c_month - b_month
				year = c_year - b_year
				print 'you are',year,'year',month,'Month','and',day,'days'
			else:
				c_year -= 1
				c_month += 12 
				c_month -= 1
				c_day += 30
				day = c_day - b_day
				month = c_month - b_month
				year = c_year - b_year
				print 'you are',year,'year',month,'Month','and',day,'days'
	else:
		list1 = [1, 3, 5, 7, 8 ,10,12]
		if is_leap(c_year) and c_month == 2:
			c_month -= 1
			c_day += 29
			day = c_day - b_day
			month = c_month - b_month
			year = c_year - b_year
			print 'you are',year,'year',month,'Month','and',day,'days'
	
		elif c_month == 2:
			c_month -= 1
			c_day += 28
			day = c_day - b_day
			month = c_month - b_month
			year = c_year - b_year
			print 'you are',year,'year',month,'Month','and',day,'days'
			
			
		elif(c_month in list1):
 			c_month -= 1
			c_day += 31
			day = c_day - b_day
			month = c_month - b_month
			year = c_year - b_year
			print 'you are',year,'year',month,'Month','and',day,'days'
		else:
			c_month -= 1
			c_day += 30
			day = c_day - b_day
			month = c_month - b_month
			year = c_year - b_year
			print 'you are',year,'year',month,'Month','and',day,'days'

if __name__ == '__main__':
	birthday()
