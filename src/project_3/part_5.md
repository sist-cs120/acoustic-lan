## ToyNet*

The current Athernet is developed by each group independently, but a real network is about opening, sharing, and cooperating. This task is to reward the groups who are able to interconnect to each other. The network topology of three connected groups is shown in the Devices section. Your goal to ensure that every NODE1x can ping each other.


### Device
- NODE1x: Sender/Replier for each group
- NODE2x: Gateway for each group

![ToyNet](/media/toynet.png)

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
