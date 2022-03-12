## Part 2 Frame Detection

**Adding a Header**. A header of a frame is used to help the receiver to find out the accurate start of a frame, i.e. synchronize to the frame. Therefore, the header is normally a predefined special wave pattern that can help with synchronization. After adding the header, samples that you are going to fill into the DAC may have the structure in Figure 3:

![](RackMultipart20220302-4-iik7fu_html_ab6f260d556ba0b9.png)

Figure 3 Adding a Header

**Frame Detection**. When the receiver receives enough samples, the first thing is to determine whether there is something transmitting. One method is to correlate the predefined header with the received samples. When the samples contains a frame, correlation will have high energy. Use this feature as the indicator of the occurrence of a frame.

**Synchronization**. Once the occurrence of a new frame is confirmed, the next thing is to find out the accurate boundaries of the symbol. You can develop your own way. One suggested way is to leverage correlation again. A unique and long header can help to find out the accurate boundary of the frame. See the Matlab example to see how to design a unique header.

### Devices
- NODE1: computer for frame detection.

### Checkpoints
-

### Tips
- Do not use a very short header. Speaker takes time to warm up (see ringing effect [1]).
