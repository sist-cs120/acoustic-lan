## Ping from External Network*

Part 3 enables ICMP echo from the network behind NAT to the Internet. Normally, ICMP echo is not able to go through a NAT gateway to the internal network from the external network. However, the payload of the ICMP packets can be leveraged to piggyback information for NAT to indicate the internal destination [5]. Suppose the NAT gateway uses static mapping, i.e., <NODE1\_IP, NODE1\_port#, NODE2\_IP, NODE2\_port#> is static. If <NODE2IP, NODE2port#> is known to the public, e.g., NODE3. NODE3 can modify the ICMP Echo Request payload through ping –p option. Define the special ICMP payload and modify the NAT gateway to support ping from the external network.

### Tips
- You can try iptables + string match to redirect ICMP packets to some listening port for NAT processing.

### Device
- NODE1: Replier, Athernet interface IP: 192.168.1.2
- NODE2: Gateway, Athernet interface IP: 192.168.1.1
- NODE3: Sender, provided by TA

### Checkpoint
- Report your ICMP payload format and content to TA.
- Report your NAT table to TA.
- Initiate NODE2 to ready Network Address Translation.
- TA run `ping <NODE2IP> -p <payload>` on NODE3
    - Payload content is decided by the group.
- NODE2 performs NAT and forward the ICMP packet to NODE1 via the Athernet interface.
- NODE1 replies with ICMP Echo Reply to NODE1. (TA's computer)
- NODE2 performs NAT and forward the ICMP packet to NODE3 via the Wifi interface.
- NODE3 should successfully receive the ICMP Echo Reply and indicate no packet loss or timeout.
