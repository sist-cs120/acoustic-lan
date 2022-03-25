# Midterm Report

## Progress
In the past weeks, I have wrapped up editing description for project 0, 1, 2. The following list the changes I've made, and the rationale behind them.

### Project 0.
- Stripped from Part 1 & 2 of original Project 1.
- First part is forming a group.
- Second part checks playing a tone, recording, and the two at same time.
- Project 0 also contains a Prequisite Self-Check for students whether this course is good fit for them. And, inform them in advance about the challenges they might face while completing the project.

### Project 1
- Transferring your first bit is now split into 3 parts.
- Part 1 tests modulation and demodulation. Modulated analog signals (samples) are saved into a csv file, as input for the demodulation. No speaker or microphone is used.
- Part 2 focuses on synchronization and frame detection. Once again analog signals are saved into a csv file, with each row representing a frame. The autograder may then add random length silence samples to the end of each frame, and perturb the signal by adding random noise. Student's implementation should still be able to detect the frame and demodulate correctly.
- Part 3 switches in the real DAC/ADC buffer instead of intermmediate file. While it might sound trivial, tuning the modulation/demodulation technique and other parameters can take quite a while. So I think it's worthwhile dedicating a separate section for parameter tuning. Moreover, it'll save students a lot of debugging time, as the correctness of their implementation is ensured in part 1 & 2.
- Bonus sections are left intact.

### Project 2
- The parts that involves jamming traditionally has been a very challenging task. I remember only 2 groups successfully completing the CSMA and CSMA/CD checkpoints on the day of checking. On the other hand, the MacPing and MacPerf utility are checked without jamming. Therefore, I propose to combine CSMA and CSMA/CD into one checkpoint, and re-order them to be after MacPing.
- The first 3 parts are mostly the same as the previous project. It's just that students now take on easier tasks (building a reliable, high-throughput, and low-latency network), before tackling on the harder ones (CSMA/CD, jamming).
- Bonus sections are left intact.

### Style changes
Each part is now divided into subsections, including
- Overview
  - Description of what to do. Potential issues, and advices are relocated to the tip section
- Devices and Network Topology
- Example
  - For MacPing and MacPerf, standardize the output format.
- Checkpoint
  - Make each steps more explicit
  - Alleviate TA's effort by using scripts (autograder) whenever possible.
- Tips


## Issues
- Design a uniform questionaire for each project?
  - It would be nice to know the design choices students made when completing the project, and why it worked for them.
    - For example, what kind of modulation techniques worked best for most students. Whether it's the baseband signal with special coding scheme, or PSK, or advanced techniques like (QAM/OFDM).
    - Plotting the preamble as a line plot. How long is it? And why is its wave form distinctive?
    - Also, their packet format. How many bits did they use for field, and why is it sufficiently large. An essential part of computer networks is designing protocols. And students show justify their protocol design choices.
    - And even ask them to draw a packet transfer diagram (like the tcp handshake one). What happens if a packet gets dropped? What if an ack gets dropped? These are the questions that students need to think through before even starting to code. Drawing diagrams of potential failures has aided me greatly in designing my own protocols and saved me tons of debugging time.

- Proposing some major changes to project 3, 4?
  - The goal of project 3 is to connect Athernet devices to the Internet. However, the NATs implemented by most students are actually proxies. Different snippets of code for TCP, UDP, and ICMP. This is mainly due to the transport / network layer protocols being implemented in the kernel. And directly modifying ip packets would require system api calls. On the other hand, many programming languages do not provide such low-level access to network interfaces. Generally, tcpstreams or udpsockets. Had to try a lot of different libraries to send/receive icmp packets.
  - Keeping the original problem sets intact, I could design an alternative project where we implement an http proxy, but sending/receiving from athernet of course. An example is [here](http://web.mit.edu/6.033/2000/www/lab/webproxy.html)
  - And project 4 would be to implement an http/1.1 server (with selected features). This way the last 2 projects could be more coherent with the first 2 projects in terms of difficulty (effort) and functionality. General impression of my classmates is that Project 3, 4 are easier thant Project 1, 2.

## Todos
- Description of project 3 & 4.
- Figures are still missing. Intend redraw them using ASCII art.
    - Make sure fits on A4 paper when printed
    - (or just extract from original work document)
- Implement autograder
- Make modification to the reference implementation accordingly
- Add more tips
