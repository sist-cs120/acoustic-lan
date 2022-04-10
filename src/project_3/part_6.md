## Part 6 TCP over Athernet


TCP is much more complex than UDP. TCP has flow control, sliding window, and congestion control components. Directly implementing TCP from scratch is not an easy task. The TCP/IP stack in current OS is implemented in the kernel, and it is also not easy to port to the Athernet. However, there are some open source TCP implantations in the user space. Refer to [4] for more information.

### Checkpoint

The check routine is similar to Part2. The network traffic is changed to the TCP protocol.
