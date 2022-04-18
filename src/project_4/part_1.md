## Part 1 FTP Client for Athernet

Unlike previous projects, FTP is a well-defined, yet quite simple protocol. Its RFC [1] is the most accurate and detailed description for guiding the implementation, thus this project description only contains a necessary introduction. As we are not going to implement an FTP server, the client part (USER-FTP) is the main focus.

At a high level, the design philosophy of FTP is simple and direct. The client uses one TCP connection (to server's port 21) to send/receive control commands/replies, and uses one or more other TCP connections to receive/upload file data. In other words, FTP's control and data planes are decoupled.

There are several FTP control commands, such as USER, PASS, PWD, CWD, PASV, LIST, RETR, STOR, etc. These commands and their responses are text-based and very similar to those used in Telnet and HTTP. Some of the commands (e.g., LIST: list current directory, RETR: download data, STOR: upload data) can initiate data transmission. Once these commands are executed, the client and server must negotiate new TCP connections to hold the data transmission. There are two methods to negotiate new TCP connections: the Passive Mode (the client connects to the port chosen by the server) and the Active Mode (server uses port 20 to connect to the port chosen by the client). Since the Athernet Node must pass through the NAT to reach the Internet, Passive Mode is the only choice if you are not going implement a stateful NAT (a stateful NAT is able to recognize/remember/modify FTP packets and open correct ports for translating connections initiated by the server in the Active Mode).

![](RackMultipart20220302-4-f4xz1s_html_30b88fb6f252c370.png)

Figure 2 Network Topology for FTP Application

### Tips:
- You may want to use Wireshark with proper filter to trace the working process of FTP.
- You can use existing FTP clients to see how they handle the input.

## Devices
- NODE1: FTP client
- NODE2: NAT
- NODE3: FTP server (Provided by TA)

The Network Topology is shown in Figure 2

### Checkpoint

- Initiate NODE2 to ready NAT
- Initiate NODE1 to start FTP client, showing a prompt for user command
- TA input commands `USER PASS PWD CWD PASV LIST RETR` and check the output
    - Credits are given according to the table below
    - For the RETR command, file is selecte by TA with size < 1MB.
- TA input invalid commands.
    - The client should print out error messages and prompt the user for another command.
    - **Crashing, exiting, hanging, or closing the connection will receive no credit.**

| Control Commands                 | Percentage |
| -------------------------------- | ---------- |
| USER PASS PWD                    | 50%        |
| USER PASS PWD CWD PASV LIST      | 83%        |
| USER PASS PWD CWD PASV LIST RETR | 100%       |

### Example
```sh
athernet --ftp-client

(ftp) USER anonymous
(ftp) PASS anonymous
(ftp) PWD
...
```
