import time

long_list = list(range(1000000))
result = []
index = 0
start_t = time.perf_counter()  # I use this to measure elapsed time
while index < len(long_list):
    result.append(long_list[0])
    index += 1
end_t = time.perf_counter()  # Here again

print(
    end_t - start_t
)  # So I can deduct the start time from the end time and I get the elapsed time


# COMMENT: Careful, this block takes on my computer almost 2 minutes
# So uncomment this at your own risk

# result = []
# start_t = time.perf_counter()
# while len(long_list) > 0:
#     result.append(long_list[0])
#     del(long_list[0])
# end_t = time.perf_counter()
# print(end_t - start_t)

# Comment: More efficient:
long_list = list(range(1000000))
result = []

start_t = time.perf_counter()
while len(long_list) > 0:
    result.append(long_list[-1])  # NB: we
    del long_list[-1]
end_t = time.perf_counter()

print(end_t - start_t)
