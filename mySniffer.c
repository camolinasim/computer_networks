#include <pcap.h>
#include <stdio.h>

/* This function will be invoked by pcap for each captured packet.
We can process each packet inside the function.
*/
void got_packet(u_char *args, const struct pcap_pkthdr *header, const u_char *packet){
   printf("Got a packet\n");
}

int main(){
   pcap_t *handle;
   //char errbuf[PCAP_ERRBUF_SIZE];
   struct bpf_program fp;
   char filter_exp[] = "tcp and port 35565";
   bpf_u_int32 net;
   const u_char *packet;		/* The actual packet */
	struct pcap_pkthdr header;	/* The header that pcap gives us */



   //step 0: creating dev
   char *dev, errbuf[PCAP_ERRBUF_SIZE];
   dev = pcap_lookupdev(errbuf);
		if (dev == NULL) {
			fprintf(stderr, "Couldn't find default device: %s\n", errbuf);
			return(2);
		}
		printf("Device: %s\n", dev);
		//return(0);
   // Step 1: Open live pcap session on NIC with name ethx
   // you need to change "eth3" to the name
   // found on their own machines (using ifconfig).
   handle = pcap_open_live("ens33", BUFSIZ, 1, 1000, errbuf);
    if (handle == NULL) {
		 fprintf(stderr, "Couldn't open device %s: %s\n", dev, errbuf);
		 return(2);
	 }
   //printf("end step 1");
   // Step 2: Compile filter_exp into BPF psuedo-code
   pcap_compile(handle, &fp, filter_exp, 0, net);
   pcap_setfilter(handle, &fp);
   // Step 3: Capture packets
   pcap_loop(handle, -1, got_packet, NULL);
   /* Grab a packet */
		packet = pcap_next(handle, &header);
	/* Print its length */
	printf("Jacked a packet with length of [%d]\n", header.len);
   pcap_close(handle); //Close the handle
   return 0;
}
// Note: don’t forget to add "-lpcap" to the compilation command.
// For example: gcc -o sniff sniff.c -lpcap