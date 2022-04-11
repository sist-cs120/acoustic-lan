## Part 3 ICMP Echo

Internet Control Message Protocol (ICMP) is one of the most import protocols running over IP. As the name suggests, ICMP targets 'control' rather than transmitting data. ICMP defines several useful messages to indicate and debug network errors. ICMP echo is the most basic one. ICMP echo defines a send and reply protocol. Whenever a receiver receives an ICMP Echo Request message, the receiver is responsible for replying an ICMP Echo Reply message to the request sender as soon as possible.

This task is to support ICMP echo in Athernet nodes, you may want to consider the following three aspects:

First, NODE1 should be able to send correct ICMP Echo Request to the Internet. In order to be able to receive replies from standard receivers, the ICMP packets must be in the correct format. Check the wiki [1] to see the ICMP format that is not covered in lectures. As Ping is based on ICMP echo, you can use Wireshark with icmp filter to capture Ping packets as the reference to create correct ICMP echo packets.

Second, NODE2 should be able to translate ICMP echo packets. As the ICMP is a protocol in IP layer (i.e., parallel to TCP/UDP), its packets have no port number, which is used as the translation key in the NAT table. However, NAT can use the identification field [1] in the ICMP payload as the identifier [2]. In other words, the <IP, ID> pair in ICMP packets has the same function as the <IP, port#> pair in TCP/UDP packets for the NAT.

Third, NODE2 should be able to send and receive ICMP echo packets to and from NODE3. ICMP echo packets, especially ICMP Echo Reply, are normally handled by the OS and are hidden to the normal socket. In order to capture the ICMP Echo Reply from NODE3, you may want to use the raw socket [4]. When forwarding ICMP Echo Request from NODE1, the raw socket is also a good choice to fully customize your packets.

### Tips
- Some network interface cards do not support raw socket.
- Some programming languages may not provide low-level access to raw sockets. You can store the ICMP packet in a temporary file and send it via the system's raw socket programming interface.
- Opening a raw socket usually requires superuser privilege.

### Device
- NODE1: Sender, Athernet interface IP: 192.168.1.2
- NODE2: Gateway, Athernet interface IP: 192.168.1.1
- NODE3 is provided by TA.

### Checkpoint 1
- Report your NAT table to TA.
- Initiate NODE2 to ready Network Address Translation.
- NODE1 sends 10 ICMP packets to NODE2 via its Athernet interface.
    - 1 packet per second.
    - Payload could be any string up to your choice. (e.g., "CS120 is fun!")
- NODE2 performs NAT and forward the ICMP packet to NODE3 via the WiFi interface.
- NODE3 replies with ICMP Echo Reply to NODE1. (TA's computer)
- NODE2 performs NAT and forward the ICMP packet to NODE1 via the Athernet interface.
- NODE1 prints the ICMP Echo Reply.
    - Format is `sender_ip:id, receiver_ip:id, latency, payload`.
    - Latency should be an integer number of milliseconds.
- **The transmission must be correctly finished within 30 seconds.**

### Checkpoint 2
- Redo the experiment with destination set to `www.baidu.com`.
