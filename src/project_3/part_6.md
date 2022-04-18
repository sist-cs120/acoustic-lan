## TCP over Athernet*

TCP is much more complex than UDP. TCP has flow control, sliding window, and congestion control components. Directly implementing TCP from scratch is not an easy task. The TCP/IP stack in current OS is implemented in the kernel, and it is also not easy to port to the Athernet. However, there are some open source TCP implementation in the user space. Refer to [4] for more information.

### Checkpoint
- Redo [Part 2](/project_3/part_2.md) with TCP protocol instead.
