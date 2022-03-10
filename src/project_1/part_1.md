## Part 1. (5 points) Transmitting Your First Bit

**Modulation**. You can choose one of the modulation methods from lecture slides or other resources (see wiki [9] or reference links [8]). There is no best choice for all situations, but there exist good ones for certain situations. For our project, FSK is easy to implement and PSK can reach high throughput. ASK is not recommended. This project description uses PSK as an example.

In PSK, suppose phase 0 is used to represent '0' and phase pi is used to represent '1'. It is easy to imagine that the wave for conveying bits is the concatenation of several wave segments in Figure 2.

![](RackMultipart20220302-4-iik7fu_html_76955159c989f910.png)

Figure 2 PSK Example

Further, suppose the carrier wave is 10 kHz and the bit rate is 1000 Hz, each wave segment in Figure 2 lasts for 1/1000 s, i.e., there are 10 cycles of the carrier wave in each segment. Similarly, if you want to reduce the bit rate to 500 Hz, each wave segment should last for 1/500 s, and there are 20 cycles in each segment. On the other hand, if the carrier wave is 20 kHz, the number of the cycles are doubled in the above description.

Now you know how to generate the modulated signals. The next step is to translate the signals into digital samples, so that DAC can play it. You have finished this step in Part2.




**Demodulation**. Demodulation is the inverse process of modulation. For PSK, multiply the received signal by the carrier wave will reveal the conveyed symbols. See the lecture slides or reference links for more information.


### Checkpoints

The group provides two devices: NODE1 and NODE2

CK1(5 points). The TA provides a TXT file 'INPUT.txt' which contains 10000 '0's or '1's. NODE1 sends bits according to this file. NODE2 stores the received bits into a TXT file 'OUTPUT.txt'. During the transmission, TAs keep quiet.

The transmission must be finished within 15 seconds.

| <15s | -0% |
| --- | --- |
| >15s | -100% |

TAs compare the difference between INPUT.txt and OUTPUT.txt through a tool similar to 'diff':

| <80% | -100% |
| --- | --- |
| 80% to 99% | -20% |
| >99% | -0% |

(Tasks with 'Optional' tag are optional tasks. The instructor is responsible for checking and grading the optional tasks. Contact the instructor to check if you have finished one or more of them. Part 4 is checked by TAs)

### Tips

a. Do not use very long frames. This is because the ADC/DAC rates of different devices are slightly different (i.e., frequency offset). For a one-second recoding, the number of samples from different devices may have differences up to ~100 samples, which will affect the synchronization for long frames.

b. Do not use a very short header. Speaker takes time to warm up (see ringing effect [1]).
