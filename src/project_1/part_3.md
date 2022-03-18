# Part 3 Transferring Your First bit

### Devices
- NODE1: computer for sending data
- NODE2: computer for receiving data


### Checkpoints
CK1(5 points). The TA provides a TXT file 'INPUT.txt' which contains 10000 '0's or '1's. NODE1 sends bits according to this file. NODE2 stores the received bits into a TXT file 'OUTPUT.txt'. During the transmission, TAs keep quiet. The transmission must be finished within 15 seconds. TAs compare the difference between INPUT.txt and OUTPUT.txt through a tool similar to 'diff':


- Time requirement

| Transmission time t | Percentage |
| ------------------- | ---------- |
| t < 15s             | 100%       |
| t > 15s             | 0%         |


- Accuracy

| Accuracy a    | Percentage |
| ------------- | ---------- |
| a > 99%       | 100%       |
| 80% < a < 99% | 80%        |
| a < 80%       | 0%         |

(Tasks with 'Optional' tag are optional tasks. The instructor is responsible for checking and grading the optional tasks. Contact the instructor to check if you have finished one or more of them. Part 4 is checked by TAs)

### Tips
- Do not use very long frames. This is because the ADC/DAC rates of different devices are slightly different (i.e., frequency offset). For a one-second recoding, the number of samples from different devices may have differences up to ~100 samples, which will affect the synchronization for long frames.
