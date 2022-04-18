## Higher Bandwidth*

The Bandwidth of your acoustic link is limited by many factors. A big one is the echoes. Echoes (i.e. signals from multiple paths) blur the boundary between the symbols/bits. Handling echoes is a challenging task. One way is to estimate the property of the echoes and try to cancel it out (see equalization [2]). Sometimes we can leverage advanced modulation (see OFDM[3]) to reduce the impact of the echoes. Some researchers have already given a good example on how to implement OFDM in acoustic channel [4]. I suggest you take a look at it. This article provide useful information for your implementation even if you are not going to implement OFDM.

### Checkpoint
- The check routine is similar to [Part 3](/project_1/part_3.md)
