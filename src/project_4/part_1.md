# Part 1 FTP Client for Athernet

Unlike previous projects, FTP is a well-defined, yet quite simple protocol. Its RFC [1] is the most accurate and detailed description for guiding the implementation, thus this project description only contains a necessary introduction. As we are not going to implement an FTP server, the client part (USER-FTP) is the main focus.

At a high level, the design philosophy of FTP is simple and direct. The client uses one TCP connection (to server's port 21) to send/receive control commands/replies, and uses one or more other TCP connections to receive/upload file data. In other words, FTP's control and data planes are decoupled.

There are several FTP control commands, such as USER, PASS, PWD, CWD, PASV, LIST, RETR, STOR, etc. These commands and their responses are text-based and very similar to those used in Telnet and HTTP. Some of the commands (e.g., LIST: list current directory, RETR: download data, STOR: upload data) can initiate data transmission. Once these commands are executed, the client and server must negotiate new TCP connections to hold the data transmission. There are two methods to negotiate new TCP connections: the Passive Mode (the client connects to the port chosen by the server) and the Active Mode (server uses port 20 to connect to the port chosen by the client). Since the Athernet Node must pass through the NAT to reach the Internet, Passive Mode is the only choice if you are not going implement a stateful NAT (a stateful NAT is able to recognize/remember/modify FTP packets and open correct ports for translating connections initiated by the server in the Active Mode).

![](RackMultipart20220302-4-f4xz1s_html_30b88fb6f252c370.png)

Figure 2 Network Topology for FTP Application

Checkpoints:

The Network Topology is shown in Figure 2

The group provides two devices: NODE1 and NODE2.

NODE3 is a public FTP Server, which supports anonymous login. The list of suggested test FTP Servers is given in 'serverlist.txt'.

CK (6 points).

NODE1: the FTP client is connected to NODE3.

NODE2: NAT

This task is graded according to the number of supported control commands of the FTP client.

The client provides an interface for TAs to input commands and displays corresponding responses from the FTP server. The FTP client must be able to be tolerant of various or even incorrect input and display correct responses.

In order to obtain corresponding credits, the client must support a full set of commands from one of the sets in the following table.

For RETR command, the downloading file is selected from FTP server by TAs and its file size is less than 1MB.

| Control Commands |
 |
| --- | --- |
| USER PASS PWD | -50% |
| USER PASS PWD CWD PASV LIST | -17% |
| USER PASS PWD CWD PASV LIST RETR | -0% |

Tips:

a. You may want to use Wireshark with proper filter to trace the working process of FTP.

b. You can use existing FTP clients to see how they handle the input.
