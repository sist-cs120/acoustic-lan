## Network Address Translation

Network Address Translation (NAT) is a design choice to connect the Athernet to the Internet. In Figure 2. NODE2 has two network interfaces. One is the WiFi interface which is used to connect to the wireless LAN. The other consists of the audio card and the previous two projects you have finished. At a high level, the two network interfaces have very similar functionalities. From the operating system's viewpoint, however, they are different. Normally, the network traffic of the OS passes through the TCP/IP stack. The WiFi interface functioning below the TCP/IP stack is one of the standard I/O devices for TCP/IP segments. However, the I/O of Project 2 hasn't been hooked to the TCP/IP stack and thus the operating system cannot recognize the Athernet interface. Thus, existing NAT tools based on TCP/IP stack cannot be directly used to realize NAT in the Athernet Gateway.

Therefore, this part is to manually build NAT for the Athernet Gateway. Check more information about NAT on Lecture Slides. In order to talk with the Internet, the traffic over Athernet must 'speak' TCP/IP, i.e., the payload of the Athernet MAC frame must contain a TCP/IP header. Specifically, if the protocol is UDP, the frame structure is shown in Figure 3. After receiving an Athernet frame like Figure 3, NODE2 is responsible for extracting <NODE1\_IP, NODE1\_port#> as the key to construct the NAT table. Also, NODE2 is responsible for repacking the UDP Payload of the Athernet frame to standard network socket with <NODE2\_IP, NODE2\_port#> and then sends it to the Internet through the WiFi interface. On the reverse direction, NODE2 should listen on the specific port# and translate the received packets to Athernet frames. After that, it transmits the frame to NODE1 via the acoustic link.

![](RackMultipart20220302-4-1606c2j_html_d2505fd8e095b784.png)

Figure 3 Frame Structure

### Tips
- If you use different programming languages to implement the Athernet transceiver and the NAT table, the network packets between them can be shared through a temporary file.

### Device
- NODE1: Sender, Athernet interface IP: 192.168.1.2
- NODE2: Gateway, Athernet interface IP: 192.168.1.1
- NODE3: Receiver

### Checkpoint 1
- Report your NAT table to TA.
- TA provides a text file `input.txt`
    - Contains 30 lines of messages.
    - The length of a message is less than 40 bytes.
    - A sample `input.txt` with two messages is provided.
- Initiate NODE3 to wait for incoming UDP packets.
- Initiate NODE2 to ready Network Address Translation.
- NODE1 sends IP packets to NODE2 via its Athernet interface.
- NODE2 extracts the UDP packet (IP payload) and sends it to NODE3 via the WiFi interface.
- NODE3 receives the UDP packet and prints it out.
- **The transmission must be correctly finished within 30 seconds.**

### Checkpoint 2
- Redo the experiment with NODE1 as the receiver and NODE3 as the sender.
