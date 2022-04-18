## Athernet Tunnel*

FTP is a classic network protocol. Many FTP client and server tools/programs exist. So the second way to enable FTP client on Athernet Nodes is to reuse existing ones (e.g. FileZilla client, ftp in linux, etc.). The problem is that the default network traffic goes through system's network stack (e.g. through socket), but not the acoustic channel. If the FTP server's IP address is known, it is possible to redirect all the traffic from/to the FTP server to a local agent/proxy program through iptables, (the port used in FTP can be found through netstat). Then, the proxy program redirects the traffic to Athernet. In this case, the FTP client works through an Athernet Tunnel.

### Checkpoints
- Make sure [Part 1](/project_4/part_1.md) is working.
- Group report to TA the existing FTP client program that they're reusing.
- Group explain to TA the implementation of their Athernet Tunnel.
- TA check implementation of the Athernet Tunnel.
