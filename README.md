# Qbuild
Build list of queries with all items from values list injected into the _INJECTION_POINT_ 


#########################################################################
#																		                                    #
#							            Made by K00B404								                #
#																		                                    #
# 	optional arguments:													                        #
#   	-h, --help           show this help message and exit			        #
#   	-L ITEMS_TO_PROCESS  list of items to inject		 			            #
#   	-Q QUERY_TO_BUILD    String to inject the values into			        #
#		  -O 																                                #
# 	Usage Example: 														                          #
#		python Qbuild.py \												                          #
#			-L '["A","B","C"]' \										                          #
#			-Q 'Select * from table where name = _INJECTION_POINT_ ;' \	      #
#			-O 'filename.txt'											                            #
#																		                                    #
#########################################################################
