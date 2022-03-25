def count_down(start):
    # count the nums down till the countDown is greater than 0
    if start > 0:
        """ Count down from a number  """
        print(start)
        count_down(start-1)

count_down(3)