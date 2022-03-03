## Part 2. (2 points) Generating Correct Sound

Knowing how to play and recode sound does not help in generating a correct sound signal. The later task is more about calculation and matching sampling rate. Suppose the sound you want to generate is f(t) and the DAC uses sample rate fs. Filling digital samples f(0), f(1/fs), f(2/fs), …, f(n/fs) into the DAC buffer will generate correct sound signal f(t) for the speaker. In this procedure, f(t) is sampled into discrete samples at rate fs.

DAC's sample rates are fixed values such as 8kHz, 16kHz, 44.1kHz, 48kHz, etc. These values are internally determined by the hardware. Choose fs from the supported rates as your desired sample rate, because any sample rates other than the supported ones are to be converted by the operating system or the media player, which could bring unexpected problems.

Checkpoints:

The group provides one device: NODE1.

CK1(2 points). NODE1 is able to play signal: f(t) = sin (2pi 1000 t) + sin (2pi 10000 t). TAs use spectrum analyzer to check the frequencies of the sound signal.

Tips:

a. You can record the sound into a file, and then use tools like Matlab/NumPy to load, plot and replay the sound in the file. It is a useful debugging technique that you will frequently use in this and future projects.

b. Window and Linux have very different architecture in handling sound [7]. You are recommended to use 44.1kHz sample rate in Linux, including Android.

c. Useful phone Apps for debugging: ATG Lite (generating pure tone), SpectrumView (viewing sound wave and spectrum)
