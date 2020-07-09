import time

tic = time.perf_counter()
# Some function
toc = time.perf_counter()

print(f"Completed the process in {toc - tic:0.4f} seconds")

