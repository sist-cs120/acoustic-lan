## MacPerf Utility

In this part of the project, you will implement a command to measure the throughput of your (reliable) acoustic link, similar to the [iperf](iperf.fr) utility. The difference, though, is that this command works in the link layer, instead of the network/transport layer.
macperf utility is used to measure the throughput between two nodes in *Athernet*. By default, MacPerf frames are generated with random payload size. The sender should try its best to send out MacPerf frames, and prints the throughput on the screen every second. 'Throughput' here is measured by the total payload size successfully acked within the 1 second window.

### Devices
- NODE1: sends macperf packets to NODE2, prints throughput every second
- NODE2: sends macperf packets to NODE1, prints throughput every second

### Checkpoint
- TA run MacPerf utility on both nodes
- TA records the throughput of both nodes for 10 seconds
- **The 10 throughput printings on both nodes should be consistently larger than 1 kbps.**


```sh
## NODE1
athernet --node 1 --macperf 2

## NODE2
athernet --node 2 --macperf 1
```
