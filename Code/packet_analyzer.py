from compute_metrics import *
from filter_packets import *
from packet_parser import *

#Peter Mastropaolo (pjm8331)
#Joshua Kelly (jmk3378)

# Run filter on each node:

try:
    #Node 1
    filter("Captures/Node1.txt")
    #Node 2
    filter("Captures/Node2.txt")
    #Node 3
    filter("Captures/Node3.txt")
    #Node 4
    filter("Captures/Node4.txt")
except FileNotFoundError:
    print("Usage: python3 Code/packet_analyzer.py")
    exit()
# Run parse on each filtered node:

#Node 1
node1_parsed = parse("Captures/Node1_filtered.txt")
#Node 2
node2_parsed = parse("Captures/Node2_filtered.txt")
#Node 3
node3_parsed = parse("Captures/Node3_filtered.txt")
#Node 4
node4_parsed = parse("Captures/Node4_filtered.txt")


# Run compute on for each node_parsed:

#Node 1
node1_data = compute("192.168.100.1", node1_parsed)
#Node 2
node2_data = compute("192.168.100.2", node2_parsed)
#Node 3
node3_data = compute("192.168.200.1", node3_parsed)
#Node 4
node4_data = compute("192.168.200.2", node4_parsed)



#Expected Return from compute is a list = [totReqSent, totReqRecv, totRepSent, totRepRecv, totReqBytesSent, totReqDataSent, totReqBytesRecv, totReqDataRecv, avgRTT, eput, gput, avgReplyDelay, avgEchoHop])

# Write node data to output file inlcuding every node:

f = open("project2_output.csv", "w")

f.write("Node 1 \n")
f.write("\nEcho Requests Sent, Echo Requests Received, Echo Replies Sent, Echo Replies Received\n")
f.write(str(round(node1_data[0], 2)) +"," + str(round(node1_data[1], 2)) + "," + str(round(node1_data[2], 2)) + "," + str(round(node1_data[3], 2)) + "\n")
f.write("Echo Request Bytes Sent (bytes), Echo Request Data Sent (bytes)\n")
f.write(str(round(node1_data[4], 2)) + "," + str(round(node1_data[5], 2)) + "\n")

f.write("Echo Request Bytes Received (bytes), Echo Request Data Received (bytes)\n")
f.write(str(round(node1_data[6], 2))+ "," + str(round(node1_data[7], 2)) + "\n")
f.write("\nAverage RTT (miliseconds)" + "," + str(round(node1_data[8], 2)))
f.write("\nEcho Request Throughput (kB/sec)" + "," + str(round(node1_data[9], 2)))
f.write("\nEcho Request Goodput (kB/sec)" + "," + str(round(node1_data[10], 2)))
f.write("\nAverage Reply Delay (microseconds)" + "," + str(round(node1_data[11], 2)))
f.write("\nAverage Echo Request Hop Count" + "," + str(round(node1_data[12], 2)) + "\n")

f.write("\n Node 2\n")
f.write("\nEcho Requests Sent, Echo Requests Received, Echo Replies Sent, Echo Replies Received\n")
f.write(str(round(node2_data[0], 2)) +"," + str(round(node2_data[1], 2)) + "," + str(round(node2_data[2], 2)) + "," + str(round(node2_data[3], 2)) + "\n")
f.write("Echo Request Bytes Sent (bytes), Echo Request Data Sent (bytes)\n")
f.write(str(round(node2_data[4], 2)) + "," + str(round(node2_data[5], 2)) + "\n")

f.write("Echo Request Bytes Received (bytes), Echo Request Data Received (bytes)\n")
f.write(str(round(node2_data[6], 2))+ "," + str(round(node2_data[7], 2)) + "\n")
f.write("\nAverage RTT (miliseconds)" + "," + str(round(node2_data[8], 2)))
f.write("\nEcho Request Throughput (kB/sec)" + "," + str(round(node2_data[9], 2)))
f.write("\nEcho Request Goodput (kB/sec)" + "," + str(round(node2_data[10], 2)))
f.write("\nAverage Reply Delay (microseconds)" + "," + str(round(node2_data[11], 2)))
f.write("\nAverage Echo Request Hop Count" + "," + str(round(node2_data[12], 2)) + "\n")

f.write("\n Node 3\n")
f.write("\nEcho Requests Sent, Echo Requests Received, Echo Replies Sent, Echo Replies Received\n")
f.write(str(round(node3_data[0], 2)) +"," + str(round(node3_data[1], 2)) + "," + str(round(node3_data[2], 2)) + "," + str(round(node3_data[3], 2)) + "\n")
f.write("Echo Request Bytes Sent (bytes), Echo Request Data Sent (bytes)\n")
f.write(str(round(node3_data[4], 2)) + "," + str(round(node3_data[5], 2)) + "\n")

f.write("Echo Request Bytes Received (bytes), Echo Request Data Received (bytes)\n")
f.write(str(round(node3_data[6], 2))+ "," + str(round(node3_data[7], 2)) + "\n")
f.write("\nAverage RTT (miliseconds)" + "," + str(round(node3_data[8], 2)))
f.write("\nEcho Request Throughput (kB/sec)" + "," + str(round(node3_data[9], 2)))
f.write("\nEcho Request Goodput (kB/sec)" + "," + str(round(node3_data[10], 2)))
f.write("\nAverage Reply Delay (microseconds)" + "," + str(round(node3_data[11], 2)))
f.write("\nAverage Echo Request Hop Count" + "," + str(round(node3_data[12], 2)) + "\n")

f.write("\n Node 4\n")
f.write("\nEcho Requests Sent, Echo Requests Received, Echo Replies Sent, Echo Replies Received\n")
f.write(str(round(node4_data[0], 2)) +"," + str(round(node4_data[1], 2)) + "," + str(round(node4_data[2], 2)) + "," + str(round(node4_data[3], 2)) + "\n")
f.write("Echo Request Bytes Sent (bytes), Echo Request Data Sent (bytes)\n")
f.write(str(round(node4_data[4], 2)) + "," + str(round(node4_data[5], 2)) + "\n")

f.write("Echo Request Bytes Received (bytes), Echo Request Data Received (bytes)\n")
f.write(str(round(node4_data[6], 2))+ "," + str(round(node4_data[7], 2)) + "\n")
f.write("\nAverage RTT (miliseconds)" + "," + str(round(node4_data[8], 2)))
f.write("\nEcho Request Throughput (kB/sec)" + "," + str(round(node4_data[9], 2)))
f.write("\nEcho Request Goodput (kB/sec)" + "," + str(round(node4_data[10], 2)))
f.write("\nAverage Reply Delay (microseconds)" + "," + str(round(node4_data[11], 2)))
f.write("\nAverage Echo Request Hop Count" + "," + str(round(node4_data[12], 2)) + "\n")

f.close()
