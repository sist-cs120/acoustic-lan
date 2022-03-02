## Part 4. (2 point) macperf Utility

macperf utility is used to measure the throughput between two nodes in _Athernet_. The utility is similar to the iperf utility, but it is specialized for _Athernet_ and works in a different layer.

The working flow of macperf utility:

- macperf is invoked by executing macperf dest\_address
- By default, macperf frame is generated with random MAC payload (choose your own payload size) and the type field of the MAC frame is set to type: DATA.
- The sender tries its best to send out macperf packets
- The sender counts and prints the throughput on the screen every one second.

Checkpoints:

The group provides two devices: NODE1, NODE2. The topology is shown in Figure 7 without jamming source.

CK(2 points). TAs will check the functionality of macping utility in the following case:

NODE1: macperf NODE2

NODE2: macperf NODE1

TAs record the throughput of NODE1 and NODE3.

| If NODE1 TH \&gt;1.0kbps &amp;&amp; NODE2 TH\&gt;1.0kbps | 100% |
| --- | --- |
| otherwise | 0% |
