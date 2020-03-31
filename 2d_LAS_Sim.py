
# SELECT WHICH ALGORITHM TO USE:

# ALGORITHM = "SRSF"
ALGORITHM = "2D-LAS"


def priority_SRSF(time_needed, n_of_gpus, time_elapsed):
    if time_needed == time_elapsed:
        return -9999
    return -(time_needed - time_elapsed) * n_of_gpus

def priority_2DLAS(time_needed, n_of_gpus, time_elapsed):
    if time_needed == time_elapsed:
        return -9999
    return -time_elapsed * n_of_gpus

# first value represents the number of n_of_gpus required and the second value represents the job duration

class Job:
    def __init__(self, n_of_gpus, time_needed):
        self.time_needed = time_needed
        self.n_of_gpus = n_of_gpus
        self.time_elapsed = 0

jobs = [Job(2,3), Job(1,4), Job(3,2), Job(2,2)]

time_elapsed = 0
jobs_finished = 0
jcts = []
while jobs_finished < 4:
    priorities = []
    for a_job in jobs:
        if (ALGORITHM == "SRSF"):
            priorities.append(priority_SRSF(a_job.time_needed, a_job.n_of_gpus, a_job.time_elapsed))
        else:
            priorities.append(priority_2DLAS(a_job.time_needed, a_job.n_of_gpus, a_job.time_elapsed))
    ind_of_job_to_do = priorities.index(max(priorities))
    print("At time: ", (time_elapsed + 1), "  Doing job: ", (ind_of_job_to_do + 1))
    jobs[ind_of_job_to_do].time_elapsed += 1
    time_elapsed += 1
    if jobs[ind_of_job_to_do].time_elapsed == jobs[ind_of_job_to_do].time_needed:
        jobs_finished += 1
        print("\tJob ", (ind_of_job_to_do + 1), " finished!")
        jcts.append(time_elapsed)
print("Total time elapsed is: ", time_elapsed)
print("Average JCT is: ", sum(jcts)/4)
