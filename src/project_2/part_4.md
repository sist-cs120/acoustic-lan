## MacPing Utility

In this part of the project, you will implement a command to measure the latency of your (reliable) acoustic link, similar to the ping utility found on both unix and windows systems. Once again, this command works in the link layer instead of the network or transport layer. Your implementation should differentiate between normal data, MacPerf and MacPing frames. To measure the latency, you will need to store the timestamp of the packet sent. Your timestamp should be of at least microsecond resolution and must not overflow within the 10 second testing period.

For example, add a MACPING/MACPONG type to the frame type field. The sender sends out one MACPING frame at a time. The receiver replies with MACPONG frame when it receives a MACPING frame. Upon receiving the MACPONG frame, the receiver should print out the round trip time of the frame. After that, the sender sends out another MACPING frame. If the sender does not receive the MACPONG frame within 2 seconds, it should print out `timed out`, and retries sending another MACPING frame.

### Devices
- NODE1: send macping packets to NODE2, prints latency for every MacPing frame successfully replied.
- NODE2: send macperf packest to NODE1, prints throughput every second.

### Checkpoint
- TA run macperf command on NODE2, and macping command on NODE1
- TA record the round trip time of NODE1 to NODE2 and the throughput of NODE3 for 10 seconds
- **NODE1 round trip time printings should be consistently lesser than 150 ms.**
- **NODE2 throughput printings should be consistently larger than 2 kbps.**

```sh
# NODE1
athernet --node 1 --macping 2

# NODE2
athernet --node 2 --macperf 1
```
