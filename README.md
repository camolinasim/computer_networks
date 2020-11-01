# computer_networks
computer networks projects

TO RUN LAB3 DO THE FOLLOWING:

Compile the program --> gcc -o snoff lab3.c -lpcap
Run it in shell --> sudo ./snoff <device_name> <filter_expression>  

Example runs in shell --> sudo ./snoff ens33 "tcp and port 23"
                      --> sudo ./snoff ens33 "icmp" 
                      --> sudo ./snoff ens33 "tcp"
                      --> sudo ./snoff ens33 "tcp and port 35565" 

