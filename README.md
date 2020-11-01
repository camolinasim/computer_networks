

To run C program:
Compile the program --> gcc -o snoff lab3.c -lpcap 
Run it in shell --> sudo ./snoff <device_name> <filter_expression> 
Example run --> sudo ./snoff ens33 “icmp”
Example run --> sudo./snoff ens33 “tcp and port 35565”
Example run → sudo ./snoff ens33 “tcp and port 23”

To run Python Program
Run it in shell --> sudo python3 skapy.py <protocol>
<protocol> -> tcp or icmp. If you choose tcp, the program will ask for a port number to listen on.

Example run: sudo python3 skapy.py tcp
After run, you will see "enter a port number to listen..."
type a port number. For example, 35565
Now the program is sniffing TCP packets in port 35565

Example run: sudo python3 skapy.py icmp
Now, the program is sniffing icmp packets. You can use the ping command now.
