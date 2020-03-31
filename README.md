# Shortest Remaining Service First (SRSF) and 2D-LAS simulator

This project implements a simple scheduling simulator to compare the SRSF algorithm with the 2D-LAS algorithm as proposed in the paper "Tiresias: A GPU Cluster Manager for Distributed Deep Learning".

The script is designed to simulate the following prompt:

"Given four DL jobs that arrive at a cluster of GPU servers at the same time. Each job is represented as a tuple which the first value represents the number of GPUs required and the second value represents the job duration.  J1 (2, 3), J2 (1, 4), J3 (3, 2), and J4 (2,2). The tie breaker is the job index. What is the schedule sequence when using shortestest-remaining-service-first scheduling and what is the job schedule sequence when using 2D-LAS? And what is the average JCT respectively?"

# Usage

Uncomment the correct line to select the appropriate algorithm and run the script.
