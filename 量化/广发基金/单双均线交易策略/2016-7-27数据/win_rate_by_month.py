# coding=utf-8  
from datetime import datetime, timedelta
import xlrd
import string
# Offset is from 0

cout = open('2016-7-27-Model-win-rate-by-month.txt', 'w')
data = xlrd.open_workbook('2016-7-27-Model' + '.xlsx')
table = data.sheets()[0]
nrows = table.nrows
date = 0
time = 0
pre_month = 1
now_month = 1
pre_year = 1
pre_wind=table.cell(3,2).value
now_wind=0
gain_wind=0
pre_net_value=table.cell(3,6).value
now_net_value=0
gain_model=0
num_of_win=0
num_of_lose=0

for i in range(3,nrows):
	date=table.cell_value(i,3)
	time = datetime(*xlrd.xldate_as_tuple(date, 0))
	if(time.month > pre_month or time.year > pre_year):
		now_wind = table.cell(i,2).value
		now_net_value= table.cell(i,6).value
		gain_wind=float(now_wind-pre_wind)/pre_wind
		gain_model=float(now_net_value-pre_net_value)/pre_net_value
		if(gain_model>=gain_wind):
			num_of_win+=1
		else:
			num_of_lose+=1
		pre_wind = now_wind
		pre_net_value = now_net_value
		pre_month=time.month
		pre_year=time.year
		cout.write(repr(time.year) + '-' + repr(time.month) + '\t' + repr(now_wind) + '\t' + repr(now_net_value) + '\t' + repr(gain_wind) + '\t' + repr(gain_model) + '\n')
cout.flush()
cout.close()
print "number of win:" + repr(num_of_win)+'\t'+"num_of_lose:"+repr(num_of_lose)


