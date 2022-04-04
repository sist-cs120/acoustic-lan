## Part 4 Ping from External Network*

Part 3 enables ICMP echo from the network behind NAT to the Internet. Normally, ICMP echo is not able to go through a NAT gateway to the internal network from the external network. However, the payload of the ICMP packets can be leveraged to piggyback information for NAT to indicate the internal destination [5]. Suppose the NAT gateway uses static mapping, i.e., <NODE1\_IP, NODE1\_port#, NODE2\_IP, NODE2\_port#> is static. If <NODE2IP, NODE2port#> is known to the public, e.g., NODE3. NODE3 can modify the ICMP Echo Request payload through ping –p option. Define the special ICMP payload and modify the NAT gateway to support ping from the external network.

Tips:

1. You can try iptables + string match to redirect ICMP packets to some listening port for NAT processing.

Checkpoints:

The group provides two devices: NODE1, NODE2

TAs provide NODE3

The network topology is shown in Figure 2.

The IP of the Athernet interface of NODE1 is 192.168.1.2, the default gateway is 192.168.1.1

The IP of the Athernet interface of NODE2 is 192.168.1.1

CK(2 points).

NODE1: receives and replies ICMP packets

NODE2: NAT

NODE3: ping NODE2\_IP -p XXXX

X is specified by the group.

NODE3 should be able to receive the ping reply from NODE1.
