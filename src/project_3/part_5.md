## Part 5 ToyNet

The current Athernet is developed by each group independently, but a real network is about opening, sharing, and cooperating. This task is to reward the groups who are able to interconnect to each other. Figure 4 is the network topology of three connected groups. Your goal to ensure that every Node1x can ping each other.

![](RackMultipart20220302-4-1606c2j_html_b6708c49f804090c.png)

Figure 4 Network Topology for Three Connected Groups

### Device
Each group provides two devices: NODE1x, NODE2x

### Tips

- You can design your own ping utility, not necessarily rely on the ping of your system, but should make sure the 'ping' packets arrived at NODE2x are ICMP pings.

### Checkpoint

- The network topology for three connected groups is shown in Figure 4.
- NODE1x of each group should be able to ping NODE1x of other groups:
- The command is similar to Part4.
- NODE1x: ping NODE2y\_IP -p XXXX
- The reward is proportional to the number of connected groups (can ping each other).

| Connected Groups | Percentage |
| --- | --- |
| 2 | -50% |
| 3 | -25% |
| 4 | -0% |
