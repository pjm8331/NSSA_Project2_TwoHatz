#Peter Mastropaolo (pjm8331)
def compute(ogSource, masterList):
	totReqSent = 0
	totReqRecv = 0
	totRepSent = 0
	totRepRecv = 0
	totReqBytesSent = 0
	totReqDataSent = 0
	totReqBytesRecv = 0
	totReqDataRecv = 0
	avgRTT = 0
	eput = 0
	gput = 0
	avgReplyDelay = 0
	avgEchoHop = 0
	ttlList = []
	reqTime = []
	repTime = []
	recvReqTime = []
	sendRepTime = []
	for entry in masterList:
		if 'request' in entry:
			if entry[2] == ogSource:
				reqTime.append([entry[0], entry[-1].strip(')'), entry[1]])
				totReqSent+=1
				totReqBytesSent+=int(entry[5])
				totReqDataSent+=(int(entry[5]) - 42)
			elif entry[3] == ogSource:
				recvReqTime.append([entry[0], entry[-1].strip(')'), entry[1]])
				totReqRecv+=1
				totReqBytesRecv+=int(entry[5])
				totReqDataRecv+=(int(entry[5]) - 42)

		elif 'reply' in entry:
			if entry[2] == ogSource:
				totRepSent+=1
				sendRepTime.append([entry[0], entry[1]])
			elif entry[3] == ogSource:
				tempttl = int(entry[-4].strip('ttl='))
				ttlList.append(129-tempttl)
				repTime.append([entry[0], entry[1]])
				totRepRecv+=1

		else:
			print("Error, not properly filtered line!")
			print(str(entry))
	avgRTT, sumRTT = getAverageRTT(reqTime, repTime)
	avgReplyDelay = getAverageReplyDelay(recvReqTime, sendRepTime)
	eput = ((totReqBytesSent / sumRTT) / 1000)
	gput = ((totReqDataSent / sumRTT) / 1000)
	avgEchoHop = sum(ttlList)/len(ttlList)
	print(sum(ttlList))
	print(len(ttlList))
	return [totReqSent, totReqRecv, totRepSent, totRepRecv, totReqBytesSent, totReqDataSent, totReqBytesRecv, totReqDataRecv, avgRTT, eput, gput, avgReplyDelay, avgEchoHop]

def getAverageRTT(reqTime,repTime):
	avg = 0
	avgList = []
	for item in reqTime:
		ReqNum = int(item[0])
		RepNum = int(item[1])
		time = float(item[2])
		for z in repTime:
			if int(z[0]) == RepNum:
				avgList.append(float(z[1])-time)
				break
	avg = ((sum(avgList) / len(avgList))*1000)
	sumRTT = sum(avgList)
	return avg, sumRTT

def getAverageReplyDelay(reqTime,repTime):
	avg = 0
	avgList = []
	for item in reqTime:
		ReqNum = int(item[0])
		RepNum = int(item[1])
		time = float(item[2])
		for z in repTime:
			if int(z[0]) == RepNum:
				avgList.append(float(z[1])-time)
				break
	avg = ((sum(avgList) / len(avgList))*1000000)
	return avg