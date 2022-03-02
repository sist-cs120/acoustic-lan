## Part 1. (3 points) Understanding Your Tools

Different operating systems have different architectures for media I/O, but their usages are quite similar. In order to convey bits through acoustic signals, you must be able to correctly send and receive through the media interface.

For playing with sound (e.g. transmitting sound samples through the speakers and sampling sound through the microphone) via your computers, you can start by referring to the Audio Stream Input/Output (ASIO) protocol [6]. ASIO is supported by most sound card drivers. Compared with the default/or common system audio interfaces, such as WindowsAudio or DirectSound, ASIO has significant improvement on the latency. The latency measures the elapse of time when a sample is &quot;written&quot; into the buffer of the sound interface and the time when the audio of that sample is actually played by the audio hardware, which matters a lot in our next project. Not surprisingly, the latency is related to the buffer size of the sound interface. But small buffer size in a loaded system might result in a discontinuous sound wave or a &quot;buzz&quot; sound. ASIO reduces the latency at its best while maintaining sound quality. ASIO has several driver implementations. ASIO4ALL [10] working in Windows is verified by me. For programming in JAVA, you can choose a JAVA wrapper [11] to access the ASIO driver. For programming in other languages, you can either call the ASIO native APIs directly or find other wrappers yourself. For Linux and MAC OS user, you can either try WineASIO or other low latency audio interfaces, but there is no guarantee on that (I haven&#39;t tried them). Here is a utility to test the latency of the chosen sound interface [12]. The latency should be within 20 ms or better (15 ms) in order to finish Project 2.

In this part, your task is to use the chosen audio interface to correctly control your sound card&#39;s ADC and DAC to play digital samples through speaker and to record analog sound signals from microphone. Playing and recoding should be able to work simultaneously, as the transmitter and the receiver of a network card normally works simultaneously. You can use two independent threads to play and record sound simultaneously.

Checkpoints:

The group provides one device: NODE1.

CK1(1.5 points). NODE1 is able to record the voice from TA (10 seconds) and then play the recorded signals.

CK2(1.5 points). NODE1 is able to play a predefined sound (any) and record the played sound at the same time. TA may say something during the recording. After 10 seconds, stop playing and recording. Then play the recorded sound for verification.

Tips:

a. Be careful about stereo settings. We only need one track

b. Be careful about the sampling rate of the ADC and DAC, match them unless you know what you are doing.
