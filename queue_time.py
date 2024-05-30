import heapq

def queue_time(customers, n):
    if not customers or not n:
        return 0

    tills = [0] * n  # Initialize each till's time to 0
    heapq.heapify(tills)  # Convert the list to a heap to efficiently find the shortest queue

    for customer_time in customers:
        # Add the next customer to the shortest queue
        next_till = heapq.heappop(tills)
        next_till += customer_time
        heapq.heappush(tills, next_till)

    # The total time required is the maximum time among all tills
    return max(tills)

def queue_time2(customers, n):
    #check to see if n > 0
    #check if the customers leng is greater than 1

    # customers_q = {i: 0 for i in range(1,n+1)}



queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the
# queue finish before the 1st person has finished.

queue_time([2,3,10], 2)
# should return 12