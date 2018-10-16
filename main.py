import csv
import sys

ipfile = sys.argv[1]
# ipfile = 'UhWireless_mon.csv'
packets = 0
count = 0
#total is number of packets counter
total = 0
# tmr is time increments in 1 second.
tmr = 1.0
prevCount = 0
prev =0
prevPacket = 0
prevEnd = 0
curPacket = 0
x = 0
y = 0
with open(ipfile, 'rb') as csvfile:
    packetreader = csv.reader(csvfile, delimiter=',')
    for row in packetreader:
        if row[0]=='No.':
            continue
        else:
            if float(row[1])<=tmr:
                count += 1
                total += 1
                #
                x = row[1]
                node = row[2]
                # print count
            else:
                y = row[1]
                prevPacket = curPacket
                curPacket = y
                prevEnd = x
                nodeIp = node
                prevCount = packets
                packets = count
                count = 1

                tmr += 1
            #check if the number of packets are greater than previous count of number of packets for a time frame.
            if packets>prev:
                prev = packets
                #Setting initial starting of growth of packets per second as surgeStartTime in milli seconds from start of packet capture
                surgeStartTime = str(prevPacket)
                #Setting peak of the surge growth as surge end time as surgeEndTime in milli seconds from start of packet capture
                surgeEndTime = str(prevEnd)
                surgeLvl = str(prev)
                # Setting Node IP as the ip address that created the surge.
                nIP = str(nodeIp)

    # Finding the average packets per second and setting it as Baselinelvl
    baselineLvl = int(total/tmr)

print "Surge Start (from start of capture): %s ms\n" \
      "Surge End Time (from start of capture): %s ms\n" \
      "Base line level: %s pkt/s\n" \
      "Surge level: %s pkt/s \n" \
      "Node Ip: %s" % (surgeStartTime, surgeEndTime, baselineLvl, surgeLvl, nIP)