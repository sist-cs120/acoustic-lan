## Part 1 Socket Programming

This part is mostly for you to get familiar with the basic socket programming. A network socket is abstraction provided by the operating system, usually exposed to the user via system programming apis (In Linux, it is the `socket()` syscall). However, directly invoking syscalls to setup sockets is not very inconvenient. Modern programming languages usually come with builtin support for TCP streams and UDP sockets in their standard library. These APIs are exposed at a higher level of abstraction, consistent with their idioms. They also reduce the need for bindings and boilerplate code. (For example, `import sockets` in python and `std::net::UdpSocket` in Rust)

You task is to write a program that can send and receive UDP packets.

![](RackMultipart20220302-4-1606c2j_html_61eb1aa84b4cdae1.png)

### Tips
- Make sure the WiFi network connection is successfully established in both nodes before programming. You can use your operating system's network utility to connect NODE2 and NODE3 to the campus Wi-Fi network `ShanghaiTech`.
- Use ipconfig/ifconfig command to find out the IP address of the node in the WiFi network. Also, make sure the two nodes can hear (ping) each other.
- Be careful about your binding IP address, especially when you have multiple network interface cards.
- Be careful about your firewall settings. You may want to disable or add whitelist in the system firewall and firewall applications when necessary.

### Device
- NODE2: sender
- NODE3: receiver

Figure 2 Network Topology
 The network topology is shown in Figure2. You can ignore NODE1 in this part.

### Checkpoint
- Report ip address and port number of NODE2 and NODE3 to TA.
- Initiate NODE3 to wait for incoming UDP packets.
- NODE2 sends 10 UDP packets to NODE3.
    - 1 packet per second.
    - Payload is 20 bytes of random alpha-numeric characters.
- NODE3 prints the received UDP packets.
    - Format is `sender_ip:sender_port, receiver_ip:receiver_port, payload`.
    - Put a line break between each packet.
    - Example `192.168.1.3:1234, 192.168.1.4:4321, ...`.
