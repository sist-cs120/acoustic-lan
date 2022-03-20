## A Simple Reliable Link

To build a CSMA MAC from ground up, a good warm up is a simple send-and-pray protocol. A state machine is helpful in describing a protocol. The state machine of the send-and-pray protocol is shown in Figure 3. The node can only be in one of the states at any moment. The transition of the state is driven by some events. The arrows connecting states identify the event and the transition direction.

From the state machine in Figure, it is clear that the node switches between Tx and Rx states, meaning that the node cannot transmit and receive at the same time (i.e., half duplex). Supporting full duplex may require more complex designs. Half duplex is the assumption of _Athernet_ nodes.

![](RackMultipart20220302-4-19oxl2x_html_35ba30d4cd80dca2.png)

Figure 3 Send-and-pray State Machine

The goal of this task is to help you polish your physical layer code. Making a clear abstraction of the functionalities of the physical layer from project 1 helps a lot in implementing MAC protocols. For example, the following primitives are necessary ones that the physical layer interface must support for implementing the above simple protocol:

- Function: PHYSend(MACFrame), is provided by PHY.Tx thread. MAC thread can call this function to send one MAC frame. The finishing of the transmission is notified by TX\_DONE event.
- Event: TX\_DONE,is issued by PHY.Tx thread, MAC thread can capture this event and process some necessary jobs (e.g., dequeuer of the FIFO). Then the state proceeds from Tx to FrameDetection.
- Event: PACKET\_DETECTED. If a packet header is detectedin PHY.Rx thread, the thread will issue this event. Once the MAC thread receives this event, it will switch to the Rx state.
- Buffer: PHYRxFrame, is shared between PHY.Rx thread and MAC thread. Once a frame is correctly received by the physical layer, PHY.Rx thread will put the frame into this buffer.
- Event: RX\_DONE, is issued by PHY.Rx thread, it notifies MAC thread to take the frame in PHYRxFrame and proceed to FrameDetection state.

It is easy to extend the send-and-pray protocol to a more effective one: stop-and-wait ACK protocol. 'Upgrading' the physical link in Project1 with ACK ability will provide reliability in data communication. A reference stop-and-wait protocol is shown in Figure 4.

![](RackMultipart20220302-4-19oxl2x_html_4baae2d3e9586ef1.png)

Figure 4 Stop-and-wait State Machine

The state machine contains more states and events than send-and-pray protocol. One obvious difference is that, after correctly receiving a frame, the node needs to reply an ACK immediately. Note that the state machine does not contain full details of this protocol. For example, when handling Tx\_DONE event, MAC thread should set timeout counter for waiting ACK, and if the ACK is not received, the packet should be retransmitted.

### Tips
- You may want to use thread safe data structures in delivering data between threads.
- The inter-frame time and time-out time should be carefully designed (refer to Lec5 and Lec6).
- You may want to use a Tee to connect the signal

### Devices
- NODE1: sender
- NODE2: receiver

### Checkpoint 1
- TA provides a random seed
- Autograder generates `input.bin` (1000 bytes) on both nodes using the provided seed.
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
| 0 < t < 10s         | 100%       |
| 10s < t < 15s       | 80%        |
| 15s < t < 20s       | 50%        |
| t >20s              | 0%         |

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
