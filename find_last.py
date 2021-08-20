# Results: Seems that check last goes quicker for less iterations. I assume this
# is the diff of for each loop. Storing list item as variable is faster than
# repeated access.

import random
from timeit import timeit


def check_last_num(nums):
    nums_sum = 0
    for num in nums:
        if num is not nums[-1]:
           nums_sum += num


def check_last_num_ind(nums):
    nums_sum = 0
    for ind in range(len(nums)):
        num = nums[ind]
        if num is not nums[-1]:
           nums_sum += num


def check_last_num_ind_acc(nums):
    nums_sum = 0
    for ind in range(len(nums)):
        if nums[ind] is not nums[-1]:
           nums_sum += nums[ind]


def skip_last_num(nums):
    nums_sum = 0
    for ind in range(len(nums) - 1):
        nums_sum += nums[ind]


def get_rand_list():
    MIN = 0
    MAX = int(1e4)
    SIZE = int(1e4)

    random.seed()

    rand_list = []
    for iter in range(SIZE):
        rand_list.append(random.randint(MIN, MAX))

    return rand_list


def main():
    ITERATIONS = int(1e4)

    print("check_last_num():\t\t\t",
          timeit("check_last_num(rand_list)", setup="from __main__ import "
                 "check_last_num, get_rand_list\n"
                 "rand_list = get_rand_list()", number=ITERATIONS))
    print("check_last_num_ind():\t\t",
          timeit("check_last_num_ind(rand_list)", setup="from __main__ import "
                 "check_last_num_ind, get_rand_list\n"
                 "rand_list = get_rand_list()", number=ITERATIONS))
    print("check_last_num_ind_acc():\t",
          timeit("check_last_num_ind_acc(rand_list)", setup="from __main__ import "
                 "check_last_num_ind_acc, get_rand_list\n"
                 "rand_list = get_rand_list()", number=ITERATIONS))
    print("skip_last_num():\t\t\t",
          timeit("skip_last_num(rand_list)", setup="from __main__ import "
                 "skip_last_num, get_rand_list\n"
                 "rand_list = get_rand_list()", number=ITERATIONS))


if __name__ == "__main__":
    main()
