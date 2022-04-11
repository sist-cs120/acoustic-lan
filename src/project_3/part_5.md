## Part 5 ToyNet

The current Athernet is developed by each group independently, but a real network is about opening, sharing, and cooperating. This task is to reward the groups who are able to interconnect to each other. Figure 4 is the network topology of three connected groups. Your goal to ensure that every Node1x can ping each other.

![](RackMultipart20220302-4-1606c2j_html_b6708c49f804090c.png)

Figure 4 Network Topology for Three Connected Groups

### Device
- NODE1x: Sender/Replier for each group
- NODE2x: Gateway for each group
- The network topology for three connected groups is shown in Figure 4.

### Tips
- You can design your own ping utility instead of relying on the `ping` utility of your operating system. But you should make sure that the packets send/replied are still valid ICMP packets.

### Checkpoint

- Redo [Part 4](/project_3/part_4.md) with NODE3 replaced by NODE2y and NODE1y of another group.
- Check all Athernet nodes can ping each other.
- The reward is proportional to the number of connected groups (can ping each other).

| Connected Groups | Percentage |
| ---------------- | ---------- |
| 2                | 50%        |
| 3                | 75%        |
| 4                | 100%       |
