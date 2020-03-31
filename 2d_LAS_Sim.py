
# SELECT WHICH ALGORITHM TO USE:

# algorithm = "SRSF"
algorithm = "2D-LAS"


# Shortest-remaining-service-first algorithm. Assumes known job completion time.
def priority_SRSF(time_needed, n_of_gpus, time_elapsed):
    return -(time_needed - time_elapsed) * n_of_gpus

# 2D LAS algorithm. Assumes no knowledge about the job completion time.
def priority_2DLAS(n_of_gpus, time_elapsed):
    return -time_elapsed * n_of_gpus


# abstraction of a job
class Job:
    jct = None  # init to no type so error is caused if left unset

    def __init__(self, n_of_gpus, time_needed, name):
        self.time_needed = time_needed
        self.n_of_gpus = n_of_gpus
        self.name = name
        self.time_elapsed = 0

    def hasFinished(self):
        return self.time_elapsed == self.time_needed

    def setJCT(self, jct):
        self.jct = jct


# Create jobs. All jobs are assumed to take at least one time unit to complete.
jobs = [Job(2,3, "J1"), Job(1,4, "J2"), Job(3,2, "J2"), Job(2,2, "J3")]

time_elapsed = 0  # keep track of time
finished_jobs = []  # list of finished jobs
while len(jobs):

    # calculate priorities for each job
    priorities = []
    for a_job in jobs:
        if (algorithm == "SRSF"):
            priorities.append(priority_SRSF(a_job.time_needed, a_job.n_of_gpus, a_job.time_elapsed))
        else:
            priorities.append(priority_2DLAS(a_job.n_of_gpus, a_job.time_elapsed))
    # determine job to be done (the one with max priority)
    job_to_do = jobs[priorities.index(max(priorities))]

    print("At time: ", (time_elapsed + 1), "  Doing job: ", job_to_do.name)

    # do job
    time_elapsed += 1
    job_to_do.time_elapsed += 1

    # determine if finished and save metrics
    if job_to_do.hasFinished():
        print("\tJob ", job_to_do.name, " finished!")
        job_to_do.setJCT(time_elapsed)
        finished_jobs.append(job_to_do)  # move job from jobs to finished_jobs
        jobs.remove(job_to_do)

print("Total time elapsed is: ", time_elapsed)
print("Average JCT is: ", sum(c.jct for c in finished_jobs)/len(finished_jobs))
