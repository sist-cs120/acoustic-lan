## `macping` Utility

macping utility is used to measure the round trip delay between two nodes in *Athernet*. The utility is similar to ping utility in current operating systems, but it is specialized for *Athernet* and works in a different layer.

The working flow of macping utility:

- macping is invoked by executing macping dest\_address
- A macping frame is generated with zero MAC payload and the type field of the MAC frame is set to type: MACPING\_REQ.
- The macping frame is timestamped when sending into the PHY layer.
- The node with dest\_address is responsible for automatically replying a frame targeting the sender and having its type field set to type: MACPING\_REPLY.
- If the sender receives MACPING\_REPLY, it calculates and prints the round trip delay on the screen.
- If the sender does not receive MACPING\_REPLY after 2 seconds, the sender prints TIMEOUT on screen.

### Devices
- NODE1: macping
- NODE2: macperf

### Checkpoints


The topology is shown in Figure 7.

CK(2 points). TAs will check the functionality of macping utility in the following case:

TAs record the RTT of NODE1 to NODE2 and the throughput of NODE3

| NODE1 RTT < 150 ms && NODE2 TH > 2.0kbps | 100% |
| --- | --- |
| otherwise | 0% |

(Tasks with 'Optional' tag are optional tasks. The instructor is responsible for checking and grading the optional tasks. Contact the instructor to check if you have finished one or more of them)
