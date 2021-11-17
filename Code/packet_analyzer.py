from compute_metrics import *
from filter_packets import *
from packet_parser import *

#Peter Mastropaolo (pjm8331)
#Joshua Kelly (jmk3378)


#Node 1
filter("name_of_file")
#Node 2
filter("name_of_file")
#Node 3
filter("name_of_file")
#Node 4
filter("name_of_file")

#Node 1
node1_parsed = parse("node1_filtered")
#Node 2
node2_parsed = parse("node1_filtered")
#Node 3
node3_parsed = parse("node1_filtered")
#Node 4
node4_parsed = parse("node1_filtered")




#Node 1
node1_data = foo("192.168.100.1", node1_parsed)
#Node 2
node2_data = foo("192.168.100.2", node2_parsed)
#Node 3
node3_data = foo("192.168.200.1", node3_parsed)
#Node 4
node4_data = foo("192.168.200.2", node4_parsed)



#Expected Return from compute is a list = [totReqSent, totReqRecv, totRepSent, totRepRecv, totReqBytesSent, totReqDataSent, totReqBytesRecv, totReqDataRecv, avgRTT, eput, gput, avgReplyDelay, avgEchoHop]

# call filter parser

 f = open("project2_output.txt", "w")

f.write("Node 1 \n")
f.write("Echo Requests Sent\tEcho Requests Recieved\tEcho Replies Sent\tEcho Replies Received")
f.write(node1_data[0] + "\t" + node1_data[1] + "\t" + node1_data[2] + node1_data[3] +"\n")
f.write("Echo Request Bytes Sent (bytes)/tEcho Request Data Sent (bytes)")
f.write(node1_data[4] + "\t" + node1_data[5] + "\n")

f.write("Echo Request Bytes Recieved (bytes)/tEcho Request Data Recieved (bytes)")
f.write(node1_data[6] + "\t" + node1_data[7] + "\n")
f.write("\nAverage RTT (miliseconds) " + node1_data[8])
f.write("Echo Request Throughput (kB/sec) " + node1_data[9])#input num here
f.write("Echo Request Goodput (kB/sec) " + node1_data[10])#input num here
f.write("Average Reply Delay (microseconds) " + node1_data[11])#input num here
f.write("Average Echo Request Hop Count " + node1_data[12])#input num here
f.write("\n")

f.write("Node 2\n")
f.write("Echo Requests Sent\tEcho Requests Recieved\tEcho Replies Sent\tEcho Replies Received")
f.write(node2_data[0] + "\t" + node2_data[1] + "\t" + node2_data[2] + node2_data[3] +"\n")
f.write("Echo Request Bytes Sent (bytes)/tEcho Request Data Sent (bytes)")
f.write(node2_data[4] + "\t" + node2_data[5] + "\n")

f.write("Echo Request Bytes Recieved (bytes)/tEcho Request Data Recieved (bytes)")
f.write(node2_data[6] + "\t" + node2_data[7] + "\n")
f.write("\nAverage RTT (miliseconds) " + node2_data[8])
f.write("Echo Request Throughput (kB/sec) " + node2_data[9])#input num here
f.write("Echo Request Goodput (kB/sec) " + node2_data[10])#input num here
f.write("Average Reply Delay (microseconds) " + node2_data[11])#input num here
f.write("Average Echo Request Hop Count " + node2_data[12])#input num here
f.write("\n")

f.write("Node 3\n")
f.write("Echo Requests Sent\tEcho Requests Recieved\tEcho Replies Sent\tEcho Replies Received")
f.write(node3_data[0] + "\t" + node3_data[1] + "\t" + node3_data[2] + node3_data[3] +"\n")
f.write("Echo Request Bytes Sent (bytes)/tEcho Request Data Sent (bytes)")
f.write(node3_data[4] + "\t" + node3_data[5] + "\n")

f.write("Echo Request Bytes Recieved (bytes)/tEcho Request Data Recieved (bytes)")
f.write(node3_data[6] + "\t" + node3_data[7] + "\n")
f.write("\nAverage RTT (miliseconds) " + node3_data[8])
f.write("Echo Request Throughput (kB/sec) " + node3_data[9])#input num here
f.write("Echo Request Goodput (kB/sec) " + node3_data[10])#input num here
f.write("Average Reply Delay (microseconds) " + node3_data[11])#input num here
f.write("Average Echo Request Hop Count " + node3_data[12])#input num here
f.write("\n")

f.write("Node 4\n")
f.write("Echo Requests Sent\tEcho Requests Recieved\tEcho Replies Sent\tEcho Replies Received")
f.write(node4_data[0] + "\t" + node4_data[1] + "\t" + node4_data[2] + node4_data[3] +"\n")
f.write("Echo Request Bytes Sent (bytes)/tEcho Request Data Sent (bytes)")
f.write(node4_data[4] + "\t" + node4_data[5] + "\n")

f.write("Echo Request Bytes Recieved (bytes)/tEcho Request Data Recieved (bytes)")
f.write(node4_data[6] + "\t" + node4_data[7] + "\n")
f.write("\nAverage RTT (miliseconds) " + node4_data[8])
f.write("Echo Request Throughput (kB/sec) " + node4_data[9])#input num here
f.write("Echo Request Goodput (kB/sec) " + node4_data[10])#input num here
f.write("Average Reply Delay (microseconds) " + node4_data[11])#input num here
f.write("Average Echo Request Hop Count " + node4_data[12])#input num here
f.write("\n")

f.close()
