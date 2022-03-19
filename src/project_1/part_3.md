## Transferring Your First bit
Now that you have implemented modulation, demodulation, and frame detection, you are ready to transfer your first bit! This part requires little code modification, but you'll need some patience in tuning your setup. Instead of writing and reading into/from a file (`framed.csv` in part 2), you will directly write and read the samples into/from your DAC/ADC buffer. Do expect, however, that you might not succeed in the first try. We suggest double checking that your hardware setup is configured properly. We also recommend tuning your parameters to a wide range values. (10Hz ~ 20000Hz for your carrier wave frequency, and a variety of preamble patterns robust against perturbation). Turning the volume too high could drastically distort your signal. Start with the lowest possible volume and increment it small steps until you reach highest fidelity. Also, pay close attention to where and how you position your speaker and microphone. A quiet environment with the microphone and speaker positioned nicely can save you tons of debugging time!

Since we are only concerned about building a physical link so far, there is no notion of "connection" or "end of transmission". Therefore you may assume that the input provided to you is fixed length (1000 bytes). Sender program exits after sending all bytes of the provide input. And the Receiver program exits after receiving enough bytes.

### Devices
- NODE1: computer for sending data
- NODE2: computer for receiving data

### Checkpoints
- TA provides a random seed
- Autograder generates `input.bin` (1000 bytes) on both nodes using the provided seed.
- Initiate NODE2, wait for NODE1 to start transmission
- Initiate NODE1, start transmission. Timer starts.
- Wait for both nodes to finish.
    - Timer stops.
    - **Transmission time should less than 10 seconds.**
    - **Both node should exit gracefully (0 exit code, no crash, no exception) after transmission is completed.**
- NODE2 writes received data into `output.bin`
- NODE2 Autograder compares `input.bin` and `output.bin`.
- Accuracy requirement

| Accuracy a    | Percentage |
| ------------- | ---------- |
| a > 99%       | 100%       |
| 80% < a < 99% | 80%        |
| a < 80%       | 0%         |
