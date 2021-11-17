from compute_metrics import *
from filter_packets import *
from packet_parser import *

#Peter Mastropaolo (pjm8331)
#Joshua Kelly (jmk3378)


#Expected Return from compute is a list = [totReqSent, totReqRecv, totRepSent, totRepRecv, totReqBytesSent, totReqDataSent, totReqBytesRecv, totReqDataRecv, avgRTT, eput, gput, avgReplyDelay, avgEchoHop]

# call filter parser

 f = open("project2_output.txt", "w")

f.write("Node 1 \n")
f.write("Echo Requests Sent\tEcho Requests Recieved\tEcho Replies Sent\n")
#Input data here
f.write("Echo Request Bytes Sent (bytes)/tEcho Request Data Sent (bytes)")
#input data here
f.write("Echo Request Bytes Recieved (bytes)/tEcho Request Data Recieved (bytes)")
#input data here
f.write("\nAverage RTT (miliseconds) ")#Input num here
f.write("Echo Request Throughput (kB/sec) ")#input num here
f.write("Echo Request Goodput (kB/sec) ")#input num here
f.write("Average Reply Delay (microseconds) ")#input num here
f.write("Average Echo Request Hop Count ")#input num here
f.write("\n")

f.write("Node 2\n")
f.write("Echo Requests Sent\tEcho Requests Recieved\tEcho Replies Sent\n")
#Input data here
f.write("Echo Request Bytes Sent (bytes)/tEcho Request Data Sent (bytes)")
#input data here
f.write("Echo Request Bytes Recieved (bytes)/tEcho Request Data Recieved (bytes)")
#input data here
f.write("\nAverage RTT (miliseconds) ")#Input num here
f.write("Echo Request Throughput (kB/sec) ")#input num here
f.write("Echo Request Goodput (kB/sec) ")#input num here
f.write("Average Reply Delay (microseconds) ")#input num here
f.write("Average Echo Request Hop Count ")#input num here

f.write("Node 3\n")
f.write("Echo Requests Sent\tEcho Requests Recieved\tEcho Replies Sent\n")
#Input data here
f.write("Echo Request Bytes Sent (bytes)/tEcho Request Data Sent (bytes)")
#input data here
f.write("Echo Request Bytes Recieved (bytes)/tEcho Request Data Recieved (bytes)")
#input data here
f.write("\nAverage RTT (miliseconds) ")#Input num here
f.write("Echo Request Throughput (kB/sec) ")#input num here
f.write("Echo Request Goodput (kB/sec) ")#input num here
f.write("Average Reply Delay (microseconds) ")#input num here
f.write("Average Echo Request Hop Count ")#input num here
f.write("\n")

f.write("Node 4\n")
f.write("Echo Requests Sent\tEcho Requests Recieved\tEcho Replies Sent\n")
#Input data here
f.write("Echo Request Bytes Sent (bytes)/tEcho Request Data Sent (bytes)")
#input data here
f.write("Echo Request Bytes Recieved (bytes)/tEcho Request Data Recieved (bytes)")
#input data here
f.write("\nAverage RTT (miliseconds) ")#Input num here
f.write("Echo Request Throughput (kB/sec) ")#input num here
f.write("Echo Request Goodput (kB/sec) ")#input num here
f.write("Average Reply Delay (microseconds) ")#input num here
f.write("Average Echo Request Hop Count ")#input num here
f.write("\n")
