# Project 2 Multiple Access

**Due Date: Nov. 8, 2020**

(16 points + 4 points)

Suggested workload: 6 FULL days

**Please read the following instructions carefully:**

- This project is to be completed by each group **individually**.
- Submit your code through Blackboard. The submission is performed by one of the group members.
- Each group needs to submit the code **once and only once**. Immediately after TAs&#39; checking.

## Overview

This project will augment the physical data communication link from Project 1 to support mutual communication among multiple nodes. The design goal of this project is very similar to Ethernet. We call it _Athernet_. As Figure 1 shows, a core component of _Athernet_ is the mechanism to manage the transmission of each transceiver so that the communication medium can be shared efficiently, i.e., the Medium Access Control (MAC) protocol.

In order to finish this project and remaining projects, the following accessories are provided. Each group is eligible to borrow one set that includes:

1. Tee\*3 [https://item.jd.com/5005384.html](https://item.jd.com/5005384.html)

2. USB Sound Card\*3 [https://item.jd.com/1804882.html](https://item.jd.com/1804882.html)

3. Line\*4 [https://item.jd.com/1192674.html](https://item.jd.com/1192674.html)

Contact TAs to borrow the accessory set.

![](RackMultipart20220302-4-19oxl2x_html_2713465d53545674.png)

Figure 1 Project2 Overview

(Hierarchy of Tasks. Tasks are graded according to their hierarchy. A full score of one part automatically guarantees the full score of its subparts. In this project, Part 1 is a subpart of Part 2 and Part 3. Part 2 is a subpart of Part 3. The hierarchy is denoted as Part1\&lt;Part2\&lt;Part3.)

### Reference and Useful Links

[1] Sora: High Performance Software Radio Using General Purpose Multi-core Processors [https://www.usenix.org/legacy/events/nsdi09/tech/full\_papers/tan/tan.pdf](https://www.usenix.org/legacy/events/nsdi09/tech/full_papers/tan/tan.pdf)

[2] WARP CSMAMAC [https://warpproject.org/trac/wiki/CSMAMAC](https://warpproject.org/trac/wiki/CSMAMAC)

[3] WARP CSMAMAC Src

[https://warpproject.org/trac/browser/ResearchApps/MAC/CSMAMAC/csmaMac.c](https://warpproject.org/trac/browser/ResearchApps/MAC/CSMAMAC/csmaMac.c)

[4] NS3 MAC Low [https://www.nsnam.org/doxygen/mac-low\_8cc\_source.html](https://www.nsnam.org/doxygen/mac-low_8cc_source.html)

[5] GNURadio MAC Report [http://gnumac.wikispaces.com/file/view/final-project.pdf](http://gnumac.wikispaces.com/file/view/final-project.pdf)

Page **17** of **17**
