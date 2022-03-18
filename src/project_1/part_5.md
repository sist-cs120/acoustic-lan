# Part 5 Error Correction Code

Current acoustic link is susceptible to noise. You can add redundancy in your bits to resist errors caused by noise. This procedure is called coding. There are many coding schemes. Refer to [5] for more information (Convolutional code and Fountain code are suggested ones in this project).

Checkpoints:

The group provides two devices: NODE1 and NODE2

CK1(2 points). The TA provides a TXT file "INPUT.txt" which contains 10000 "0"s or "1"s. NODE1 sends bits according to this file. NODE2 stores the received bits into a TXT file "OUTPUT.txt". During the transmission, TAs will clap their hands for four times.

The transmission must be finished within 30 seconds.
<30s 	-0%
>30s 	-100%

TAs compare the difference between INPUT.txt and OUTPUT.txt through a tool similar to "diff":
<100% 	-100%
100% 	-0%
