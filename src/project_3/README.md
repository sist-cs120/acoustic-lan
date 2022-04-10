# Project 3 Gateway

(8 points + 11 points)

Suggested workload: 2~4 FULL days

### Overview
Past projects have been mostly focused on the physical link and reliable transmission, which is mainly point-to-point. In this project, we'll be connecting the Athernet nodes to the Internet. Unfortunately, a challenge remains that Athernet and Internet devices talks differently (i.e. they use different protocols). Therefore, the goal of this project is to build a gateway for the Athernet. A network gateway may contain multiple network functions, including DHCP server, routing, switching and so on. This project focuses on the aspect of interconnecting different protocols, i.e., how to translate Athernet traffic to run on existing Internet infrastructure, and vice versa. After finishing this project, the TCP/IP traffic should be able to run over the Athernet network that you have built in Project2.

We consider the situation in Figure 1, where Athernet nodes connect to an Athernet Gateway, and then get access to the Internet (the Athernet Gateway gets access to the Internet through the WiFi Access point, which is the gateway for the Athernet Gateway. It's not uncommon for such hierarchical gateways in today's Internet).

![](RackMultipart20220302-4-1606c2j_html_123832be5d807882.png)

Figure 1 Project3 Overview

The functionality of the Athernet Gateway can be as simple as a bridge, i.e., decoding the Athernet payload and repacking it into WiFi packets, and vice versa, but the problem is that the Athernet Node must be able to handle WiFi authentication, DHCP and many subtle details, which may complicate our project.

Another design choice is shown in Figure1. On the one hand, the Athernet Gateway handles the WiFi connection with existing utilities from OS. On the other hand, it handles Athernet connections from Athernet Nodes. Note that in this situation, Athernet nodes are out of the domain of the WiFi network, and thus require a different IP subnet for addressing. Since we lack independent IP addresses, NAT is required in the Athernet Gateway to translate the Athernet traffic.

(Hierarchy of Tasks. Tasks are graded according to their hierarchy. A full score of one part automatically guarantees the full score of its subparts. In this project, the hierarchy is denoted as `Part1<Part2; Part1<Part3<Part5; Part4<Part5`.)


### Reference and Useful Links

[1] ICMP Echo [https://en.wikipedia.org/wiki/Ping\_(networking\_utility)](https://en.wikipedia.org/wiki/Ping_(networking_utility))

[2] NAT RFC [https://tools.ietf.org/html/rfc3022](https://tools.ietf.org/html/rfc3022)

[3] Raw Socket [https://tangentsoft.net/wskfaq/examples/rawping.html](https://tangentsoft.net/wskfaq/examples/rawping.html)

[4] User Space TCP [http://savannah.nongnu.org/projects/lwip/](http://savannah.nongnu.org/projects/lwip/)

[5] Ping through NAT [https://stackoverflow.com/questions/4769587/is-it-possible-pinging-through-nat-from-outside-the-nat-inside](https://stackoverflow.com/questions/4769587/is-it-possible-pinging-through-nat-from-outside-the-nat-inside)

Page **7** of **8**
