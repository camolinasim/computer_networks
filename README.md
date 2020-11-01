

To run C program:
Compile the program --> gcc -o snoff lab3.c -lpcap 
Run it in shell --> sudo ./snoff <device_name> <filter_expression> 
Example run --> sudo ./snoff ens33 “icmp”
Example run --> sudo./snoff ens33 “tcp and port 35565”
Example run --> sudo ./snoff ens33 “tcp and port 23”

To run Python Program type the following in shell:
     sudo python3 skapy.py <device_name> <filter_expression>

ex:  sudo python3 skapy.py ens33 "tcp and port 23"
ex:  sudo python3 skapy.py ens33 "icmp"
