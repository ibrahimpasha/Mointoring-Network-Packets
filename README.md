### 4. Python Program to calculate Surge Levels 
I have took the sample packets captured in campus on UHWireless network and exported the packets in CSV file format. The csv file is the input to my program. Looping through every row in the input I have calculated baseline level by calculating average of total number of packets by total time frame. Then calculated surge levels by calculating sudden increase in the number of packets per second that are greater than pervious time frame. Then recorded the surge start time and surge end time. Recorded the surge level by number of packets in surge by time frame. Then noted the IP address of node that created the surge.

Input: CSV file

Calculations:
Surge Start Time: Starting Time at which surge started. Calculated by recording the Time of packet that caused the surge.
Surge End Time: Recorded the Time of packet at which number of packets per seconds reaches maximum level.
Baseline Level: Recorded by calculating the average of total number of packets in capture by total time frame.
Surge Level: Recorded by calculating the number of packets per second in surge time frame.
Node IP: Recorded the IP address of the packet at surge start level that caused the maximum number of packets per second.

##### Steps to run:
python main.py <input_file.csv>

In my case input_file is UHWireless_mon.csv

##### Sample Output:
Surge Start (from start of capture): 65.001542939 ms
Surge End Time (from start of capture): 65.999709933 ms
Base line level: 1608 pkt/s
Surge level: 5619 pkt/s 
Node Ip: ArubaNet_7f:e8:d1 (18:64:72:7f:e8:d1) (TA)

