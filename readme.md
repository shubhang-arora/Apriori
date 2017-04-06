

**Name** <br>
    Apriori Algorithm Implementation in C++ with visualisation in
    python

**SYNOPSIS** <br>
    ./a.out [support_value] [input_file] >> [output_file]

**DESCRIPTION** <br>
     Implementing the apriori association rule mining algorithm 
     using C++ to implement the algorithm itself and python to 
     visualise the results derived after running the algorithm. 
     ZIPF distribution law was used to do a fair distribution 
     of the frequencies of the items. 

**FILES** <br>
     genzipf.c
          This file generates the input values based on Zipf 
     apriori.cpp
          Code written in C++ to implement Apriori Algorithm for 
          generating frequent itemsets
     visualise.py
          Code written in Python to visualise the most frequent
          itemsets.
     stdc.h
          header files collection to run apriori.cpp
          
**USAGE** <br>
     Input Generation
          ./a.out
     Apriori Algorithm
          ./a.out <support_value> <input_file> >> <output_file>
     Visualisation
           python visualise.py <input_file_name>

**DIAGNOSTICS** <br>
     Memory Usage:
	- valgrind --tool=massif --time-unit=ms ./a.out 5 
	  mynewinput.txt >> output.txt
	- ms_print massif.out.37501
	
	For the support value of 5 and 3000 transactions, the pro-
	-gram takes around 9.180 MB



**AUTHOR** <br>
   Shubhang Arora 1410110399
   Sidharth Shanker Singh 1410110413
   Ishan Singh 1410110163 

