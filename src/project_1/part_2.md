## Frame Detection

A problem with excessively long frame is that the sender and receiver could get out of sync. This is because the ADC/DAC rates of different devices are slightly different i.e., frequency offset. For a one-second recoding, the number of samples from different devices may have differences up to ~100 samples. Depending on the modulation technique you use, this may have an adverse effect on the accuracy of the transmitted data. Take PSK for example, if the sender and the receiver is skewed by half a cycle of the carrier wave, then a `1` will be interpreted `0` and vice versa.

To combat this issue, we periodically synchronize the receiver and sender. We do this by adding a **preamble** and keeping frames short. A preamble is distinctive pattern that signals the beginning of a frame. Unlike Ethernet preamble, which is a unique bit sequence, we'll use analog signals to represent the preamble. A preamble that has worked well for most student in past semesters is a sinusoid with first increasing then decreasing frequencies. Frame detection usually starts by collecting samples into a buffer. Once the buffer is filled enough samples (longer than the length of the preamble), repeatedly compute the **autocorrelation** of the received signal with the preamble, i.e. taking the dot product of the collected samples and the predefined preamble samples. The autocorrelation is significantly larger when the collected samples exactly matches the preamble than when the samples are slightly shifted, or is computed against some random noise. Thus we can detect the presence of a frame by setting a threshold on the autocorrelation. Once the occurrence of a new frame is confirmed, the next thing is to find out the accurate boundaries of the symbol. You can develop your own way. One suggested way is to leverage autocorrelation again. A unique and long preamble can help to find out the accurate boundary of the frame. See the Matlab example to see how to design a unique header.

![Frame Detection](/media/phy_frame.png)

### Devices
- NODE1: computer for frame detection.

### Checkpoint
- Plot the shape of your preamble (lineplot).
    - The y-axis should be the sample value.
    - The x-axis should be the sample index (time).
    - Normalize your samples values to the range of [-1, 1].

- Autograder generates a binary file `input.bin` as the input, (a sequence of random bits).
    - NODE1 first breaks `input.bin` into smaller frames.
    - NODE1 then modulates each frame into real numbers.
        - Samples are delimited using a comma `,`
        - Frames are separated using a line break `\n` (or `\r\n` depending on your system)
        - Output is written to `framed.csv`, which is a csv file containing floating point matrix.
    - Autograder inserts random silence in between frames, add guassian noise, and writes output to `perturbed.csv`.
    - NODE1 takes `perturbed.csv`, demodulates frames into `output.bin`
    - Autograder compares `input.bin` and `output.bin`.
    - **The 2 files should be identical.**

```sh
athernet --modulate --framed < input.bin > framed.csv
autograder.py --perturb < framed.csv > perturbed.csv
athernet --demodulate --framed < perturbed.csv > output.bin

# One-liner using pipes
# athernet --modulate --framed < input.bin | autograder.py --perturb | athernet --demodulate > output.bin
# autograde.py --diff input.bin output.bin
```
### Tips
- Do not use a very short header. Speaker takes time to warm up (see ringing effect [1]).
