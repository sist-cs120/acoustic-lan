## Part 7. (Optional + 2 points) Performance Rank

Network systems always demand high performance, but high performance is hard to achieve. This task is to reward groups who will have achieved high throughput performance. In the first round, top 5 groups are selected according to their throughput performance in Part3. The second round will be held on the lecture, the final rank is determined by the performance in the second round.

Checkpoints:

Check settings are alomost the same as Part3.

TAs provide one Jamming source.

The group provides the interface to connect the jamming source.

The topology is shown in Figure 7.

CK(4 points). &quot;INPUT1to2.bin&quot; of 2MB and &quot;INPUT2to1.bin&quot; of 1MB are provided.

NODE1: transmits INPUT1to2.bin to NODE2, store the received file to OUTPUT2to1.bin

NODE2: transmits INPUT2to1.bin to NODE1, store the received file to OUTPUT1to2.bin

Jamming Src: play &quot;Jamming.wav&quot;

The transmission of NODE2 must be started immediately after the start of NODE1. The transmission of NODE2 must be finished before NODE1. The received files must be error free. The rank is determined by the transmission time of NODE1.

| Rank | Points |
| --- | --- |
| 1 | 100% |
| 2 | 50% |
| 3 | 25% |
| 4 | 12.5% |
| 5 | 0% |
