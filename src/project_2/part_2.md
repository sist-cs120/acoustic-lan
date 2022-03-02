## Part 2. (6 points) A Simple Reliable Link

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

It is easy to extend the send-and-pray protocol to a more effective one: stop-and-wait ACK protocol. &quot;Upgrading&quot; the physical link in Project1 with ACK ability will provide reliability in data communication. A reference stop-and-wait protocol is shown in Figure 4.

![](RackMultipart20220302-4-19oxl2x_html_4baae2d3e9586ef1.png)

Figure 4 Stop-and-wait State Machine

The state machine contains more states and events than send-and-pray protocol. One obvious difference is that, after correctly receiving a frame, the node needs to reply an ACK immediately. Note that the state machine does not contain full details of this protocol. For example, when handling Tx\_DONE event, MAC thread should set timeout counter for waiting ACK, and if the ACK is not received, the packet should be retransmitted.

Checkpoints:

The group provides two devices: NODE1 and NODE2, connected by two cables.

CK1(2 points). Similar to Part 1. TAs provide a binary file &quot;INPUT.bin&quot; which contains 6250 bytes. NODE1 sends bits according to this file. NODE2 stores the received bytes into a binary file &quot;OUTPUT.bin&quot;.

The transmission must be finished within 20 seconds.

| Transmission Time | Points |
| --- | --- |
| \&lt;10s | 100% |
| [0, 10s] | 100% |
| (10s, 15s] | 80% |
| (15s, 20s] | 50% |
| \&gt;20s | 0% |

TAs compare the difference between INPUT.bin and OUTPUT.bin:

| \&lt;100% | \*0% |
| --- | --- |
| 100% | \*100% |

CK2(2 points). Redo CK2. TAs can unplug one of the wires, and the transmitter should be able to identify the event and display &quot;link error&quot; (according to retransmission times).

Tips:

a. You may want to use thread safe data structures in delivering data between threads.

b. The inter-frame time and time-out time should be carefully designed (refer to Lec5 and Lec6).

c. You may want to use a Tee to connect the signal
