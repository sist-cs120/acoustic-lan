## Part 1 Socket Programming

The first step to build a gateway is to manipulate the TCP/IP traffic. Although different operating systems handle network traffic differently, they provide a similar interface to send/receive TCP/IP packets: the Network Socket. Refer to the textbook for more information about socket programming in C/C++. You can also use Python wrapper for socket API. If you are using Java, be noted that native Java socket API lacks the ability to manipulate raw IP packets and thus you might need to either find third party Java packages for low level socket or integrate Java with other language to finish Part3.

To get you familiar with socket programming, this part is to set up a UDP server/client pair through socket API. The network topology is shown in Figure2. You can ignore NODE1 in this part. Make sure the WiFi network connection is successfully established in both nodes before programming. You can use system's network utility to connect NODE2 and NODE3 to the campus Wi-Fi network 'ShanghaiTech'. Use ipconfig/ifconfig command to find out the IP address of the node in the WiFi network. Also, make sure the two nodes can hear (ping) each other.

Socket API provides a convenient interface to send and receive UDP packets. Write a program to send a UDP packet with 20-byte random payload from NODE2 to NODE3 every 1 second. NODE3 should be able to display the received content.

![](RackMultipart20220302-4-1606c2j_html_61eb1aa84b4cdae1.png)

Figure 2 Network Topology

Checkpoints:

The group provides two devices: NODE2 and NODE3

CK (2 points).

NODE2: transmits UDP packets to NODE3 once per second for 10 seconds

NODE3: displays IP, ports and payload of the received UDP packets.

Tips:

a. Be careful about your binding IP address, especially when you have multiple network interface cards.

b. Be careful about your firewall settings. You may want to disable or add whitelist in the system firewall and firewall applications when necessary.
