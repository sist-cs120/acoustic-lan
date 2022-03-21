## A Simple Reliable Link

Up till now, we have been using an unreliable link to transmit data. If the physical frame is corrupted or dropped, there is way of knowing it. Thus the goal of this part to implement a reliable link. To ensure data integrity, add a checksum field to your mac frame. Additionally, the receiver should send an ACK frame to the sender acknowledging the frame is received correctly. (Consider adding a type/ack field) We do not impose restriction on the implementation of your reliable link. Whether it is half or full duplex, since there are now 2 (wires) instead of 1 channel (air). To get you bootstrapped, take a look at the simple stop-and-wait state machine defined in the [appendix](/project_2/appendix.md).

### Tips
- You may want to use thread safe data structures in delivering data between threads.
- The inter-frame time and time-out time should be carefully designed (refer to Lec5 and Lec6).
- You may want to use a Tee to connect the signal

### Devices
- NODE1: sender
- NODE2: receiver

### Checkpoint 1
- TA provides a random seed
- Autograder generates `input.bin` (5000 bytes) on both nodes using the provided seed.
- Initiate NODE2, wait for NODE1 to start transmission
- Initiate NODE1, start transmission. Timer starts.
- Wait for both nodes to finish.
    - Timer stops.
    - **Both node should exit gracefully (0 exit code, no crash, no exception) after transmission is completed.**
- NODE2 writes received data into `output.bin`
- NODE2 Autograder compares `input.bin` and `output.bin`.
- Timing requirement

| Transmission Time t | Percentage |
| ------------------- | ---------- |
| 0 < t < 8s          | 100%       |
| 8s < t < 12s        | 80%        |
| 12s < t < 16s       | 50%        |
| t > 16s             | 0%         |

- Accuracy requirement

| Accuracy a    | Percentage |
| ------------- | ---------- |
| a < 80%       | 0%         |
| 80% < a < 99% | 80%        |
| a > 99%       | 100%       |

### Checkpoint 2
- Redo Checkpoint 1
- While transimission is in progress, TA unplug one of the wires.
- NODE1 should identify link failure and display `link error`. (according to retransmission times)
- Behavior of NODE2 is undefined.
