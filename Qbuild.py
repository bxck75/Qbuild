#!/usr/bin/env python


#########################################################################
#																		#
#							Made by K00B404								#
#																		#
# 	usage: Qbuild.py [-h] [-L ITEMS_TO_PROCESS] [-Q QUERY_TO_BUILD]		#
#																		#
# 	optional arguments:													#
#   	-h, --help           show this help message and exit			#
#   	-L ITEMS_TO_PROCESS  list of items to inject		 			#
#   	-Q QUERY_TO_BUILD    String to inject the values into			#
#		-O 																#
# 	Usage Example: 														#
#		python Qbuild.py \												#
#			-L '["A","B","C"]' \										#
#			-Q 'Select * from table where name = _INJECTION_POINT_ ;' \	#
#			-O 'filename.txt'											#
#																		#
#########################################################################

import sys,os,argparse,ast

ItemList = 	[]
QList = 	[]
OutputL = 	[]

parser = argparse.ArgumentParser()
parser.add_argument('-L', action='store',
					dest='items_to_process',
					type=str,
					default='Not Defined',
					help='list of items to iterate through')
parser.add_argument('-Q', action='store',
					dest='query_to_build',
					type=str,
					default='Not Defined',
					help='String to inject the values from items in')
parser.add_argument('-O', action='store',
					dest='mode',
					default='Not Defined'
					help='Outputmode File/Screen')
results = parser.parse_args()

ItemList = ast.literal_eval(results.items_to_process)
QList.append(results.query_to_build)
for x in range(len(ItemList)):
	OutputL.append(QList[0].replace('_INJECTION_POINT_', str(ItemList[x])))

#print OutputL[:]
for i in OutputL:
	print i
