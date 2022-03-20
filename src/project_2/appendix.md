## Appendix


To build a CSMA MAC from ground up, a good warm up is a simple send-and-pray protocol. A state machine is helpful in describing a protocol. The state machine of the send-and-pray protocol is shown in Figure 3. The node can only be in one of the states at any moment. The transition of the state is driven by some events. The arrows connecting states identify the event and the transition direction.

figure 3 send-and-pray state machine

![](RackMultipart20220302-4-19oxl2x_html_35ba30d4cd80dca2.png)

the goal of this task is to help you polish your physical layer code. making a clear abstraction of the functionalities of the physical layer from project 1 helps a lot in implementing mac protocols. for example, the following primitives are necessary ones that the physical layer interface must support for implementing the above simple protocol:

- function: physend(macframe), is provided by phy.tx thread. mac thread can call this function to send one mac frame. the finishing of the transmission is notified by tx\_done event.
- event: tx\_done,is issued by phy.tx thread, mac thread can capture this event and process some necessary jobs (e.g., dequeuer of the fifo). then the state proceeds from tx to framedetection.
- event: packet\_detected. if a packet header is detectedin phy.rx thread, the thread will issue this event. once the mac thread receives this event, it will switch to the rx state.
- buffer: phyrxframe, is shared between phy.rx thread and mac thread. once a frame is correctly received by the physical layer, phy.rx thread will put the frame into this buffer.
- event: rx\_done, is issued by phy.rx thread, it notifies mac thread to take the frame in phyrxframe and proceed to framedetection state.

it is easy to extend the send-and-pray protocol to a more effective one: stop-and-wait ack protocol. 'upgrading' the physical link in project1 with ack ability will provide reliability in data communication. a reference stop-and-wait protocol is shown in figure 4.

![](RackMultipart20220302-4-19oxl2x_html_4baae2d3e9586ef1.png)

Figure 4 Stop-and-wait State Machine

The state machine contains more states and events than send-and-pray protocol. One obvious difference is that, after correctly receiving a frame, the node needs to reply an ACK immediately. Note that the state machine does not contain full details of this protocol. For example, when handling Tx\_DONE event, MAC thread should set timeout counter for waiting ACK, and if the ACK is not received, the packet should be retransmitted.
