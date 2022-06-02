#!/usr/bin/env python3

import argparse
import random
import subprocess


# Generate random bytes of a given length
# Write the bytes to a file with a given name
def generate_random_bytes(length, filename):
    # Generate random bytes
    random_bytes = bytearray(length)
    for i in range(length):
        random_bytes[i] = random.randint(0, 255)

    # Write bytes to file
    with open(filename, "wb") as f:
        f.write(random_bytes)


# Read frames from a csv file
# Each row in the csv file is a frame
# Append random number of zeros to the end of each frame
# Peturb the samples in each frame with a gaussian noise
# Mean is 0 and variance is given
# Write the peturbed frames to a file named `perturbed.csv`
def perturb_frames(csv_file, mean=0, variance=1e-6):
    # Read frames from csv file
    frames = []
    with open(csv_file, "r") as f:
        for line in f:
            frames.append(line.strip().split(","))

    # Append random number of zeros to the end of each frame
    for i in range(len(frames)):
        frames[i][0] = frames[i][0] + ",0" * random.randint(0, 10)

    # Peturb the samples in each frame with a gaussian noise
    for i in range(len(frames)):
        for j in range(len(frames[i])):
            if j != 0:
                frames[i][j] = str(
                    float(frames[i][j]) + random.gauss(mean, variance), 2
                )

    # Write the peturbed frames to a file named `perturbed.csv`
    with open("perturbed.csv", "w") as f:
        for frame in frames:
            f.write(",".join(frame) + "\n")


# Autograder generates a binary file input.bin as the input, (a sequence of random bits).
# Invoke `athernet --modulate < input.bin > modulated.csv`
# Invoked `athernet --demodulate < modulated.csv > output.bin`
# Autograder compare input.bin and output.bin.
# The 2 files should be exactly the same.
def test_modulation(athernet):
    # Generate random bytes
    generate_random_bytes(100, "input.bin")

    # Write `input.bin` to stdin of athernet and capture stdout into `modulated.csv`
    with open("input.bin", "rb") as f:
        with open("modulated.csv", "w") as f2:
            subprocess.run([athernet, "--modulate"], stdin=f, stdout=f2, check=True)

    # Write `modulated.csv` to stdin of athernet and capture stdout into `output.bin`
    with open("modulated.csv", "r") as f:
        with open("output.bin", "wb") as f2:
            subprocess.run([athernet, "--demodulate"], stdin=f, stdout=f2, check=True)

    # Compare `input.bin` and `output.bin`
    with open("input.bin", "rb") as f:
        with open("output.bin", "rb") as f2:
            if f.read() != f2.read():
                print("Modulation test failed")
                exit(1)
            else:
                print("Modulation test passed")


# Autograder generates a binary file input.bin as the input, (a sequence of random bits).
# Invoke `athernet --modulate --framed < input.bin > framed.csv`
# Autograder inserts random silence in between frames, add guassian noise, and writes output to perturbed.csv.
# Invoke `athernet --demodulate --framed < perturbed.csv > output.bin`
# Autograder compares input.bin and output.bin.
# The 2 files should be identical.
def test_frame_detection(athernet):
    # Generate random bytes
    generate_random_bytes(100, "input.bin")

    # Write `input.bin` to stdin of athernet and capture stdout into `framed.csv`
    with open("input.bin", "rb") as f:
        with open("framed.csv", "w") as f2:
            subprocess.run(
                [athernet, "--modulate", "--framed"], stdin=f, stdout=f2, check=True
            )

    # Autograder perturbs the frames
    perturb_frames("framed.csv")

    # Write `perturbed.csv` to stdin of athernet and capture stdout into `output.bin`
    with open("perturbed.csv", "r") as f:
        with open("output.bin", "wb") as f2:
            subprocess.run(
                [athernet, "--demodulate", "--framed"], stdin=f, stdout=f2, check=True
            )

    # Compare `input.bin` and `output.bin`
    with open("input.bin", "rb") as f:
        with open("output.bin", "rb") as f2:
            if f.read() != f2.read():
                print("Frame detection test failed")
                exit(1)
            else:
                print("Frame detection test passed")


# Argument parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--cmd", type=str, help="Command to invoke athernet program", default="athernet"
    )
    parser.add_argument(
        "--gen-rand-bytes",
        type=int,
        default="input.bin",
        help="Generate random bytes of given length",
    )
    parser.add_argument(
        "--test",
        type=str,
        choices=["modulation", "frame_detection"],
        help="Test to run",
    )
    args = parser.parse_args()

    if args.test == "modulation":
        test_modulation(args.cmd)
    elif args.test == "frame_detection":
        test_frame_detection(args.cmd)
    elif args.gen_rand_file:
        generate_random_bytes(100, args.gen_rand_file)
