## Modulation and Demodulation

In this part you will perform modulation and demodulation. That is, converting digital signals into analog waves. For modulation, Your program should take binary files as input and output a csv containing real values. For demodulation, your program should take a csv file containing floating point numbers as input and output the demodulated file. You won't need to fiddle with the speaker and microphone just yet.

**Modulation**. You can choose one of the modulation methods from lecture slides or other resources (see wiki [9] or reference links [8]). There is no best choice for all situations, but there exist good ones for certain situations. For our project, FSK is easy to implement and PSK can reach high throughput. ASK is not recommended. This project description uses PSK as an example.

In PSK, suppose phase 0 is used to represent '0' and phase pi is used to represent '1'. It is easy to imagine that the wave for conveying bits is the concatenation of several wave segments in Figure 2.

![](RackMultipart20220302-4-iik7fu_html_76955159c989f910.png)

Figure 2 PSK Example

Further, suppose the carrier wave is 10 kHz and the bit rate is 1000 Hz, each wave segment in Figure 2 lasts for 1/1000 s, i.e., there are 10 cycles of the carrier wave in each segment. Similarly, if you want to reduce the bit rate to 500 Hz, each wave segment should last for 1/500 s, and there are 20 cycles in each segment. On the other hand, if the carrier wave is 20 kHz, the number of the cycles are doubled in the above description.


**Demodulation**. Now you know how to generate the modulated signals. The next step is to translate the signals into digital samples, so that DAC can play it. You have finished this step in Part2. Demodulation is the inverse process of modulation. For PSK, multiply the received signal by the carrier wave will reveal the conveyed symbols. See the lecture slides or reference links for more information.

### Devices
- NODE1: A single computer performing modulation and demodulation.

### Checkpoint
- Autograder generates a binary file `input.bin` as the input, (a sequence of random bits).
- NODE1 modulates `input.bin` into real numbers, and outputs to `modulated.csv`
    - a csv file containing floating point numbers in each line.
- Taking `modulated.csv` as input, NODE1 then demodulates the signal and outputs to `output.bin`.
- Autograder compare `input.bin` and `output.bin`.
- **The 2 files should be exactly the same.**

```sh
athernet --modulate < input.bin > modulated.csv
athernet --demodulate < modulated.csv > output.bin

# One-liner using pipes
# athernet --modulate < input.bin | athernet --demodulate > output.bin
# autograder.py --diff input.bin output.bin
```

### Tips
