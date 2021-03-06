## The NAT Should be an NAT Only

One possible implementation of Part 1 satisfying the check points is to make the NAT as an FTP proxy. The NAT decodes Athernet packets and, according the content, issues FTP commands locally to the remote server. However, an NAT should not work beyond the IP layer. A more serious concern is security. It does not make sense to let the NAT know your FTP password and the implementation cannot be extended to secure FTP protocols that widely used today, e.g., SFTP. In short, the NAT should be transparent to the FTP protocol. It is the Athernet Note that makes TCP connections to the FTP server other than the NAT node.

Therefore, the first component of this part is an Athernet TCP stack. FTP is based on TCP, but a full TCP stack is very complicated. In order to simplify the implementation, a simplified TCP stack in Athernet is needed to keep necessary components in TCP: connection establishment, connection termination, and sliding window. For connection establishment and connection termination, you only need to consider common cases in the TCP state machine (see lecture slides). The sliding window can be simplified to a 'stop-and-wait' protocol, where the Athernet Node generates and replies TCP acks like a 'stop-and-wait' protocol. The second component of this part is the FTP stack based on the TCP stack. The protocol state machine is provided by the FTP RFC file in the reference link.

The check procedures and requirements of part 2 are identical to part 1. Their hierarchy is part1< part2. The reason for splitting Part 2 from Part 1 is to emphasis the design philosophy of network protocols and also to ease this project.

### Checkpoint
- Make sure [Part 1](/project_4/part_1.md) is completed.
- TA check implementation of the TCP stack and FTP stack
