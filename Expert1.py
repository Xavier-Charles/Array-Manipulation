def arrayManipulationold(n, queries):
    # Create a list of zeros
    array= [0]*n
    # Repeatedly add according to the given queries
    for q in queries:
       for i in range(abs(q[0] - q[1])+1):
           if q[0] < q[1]:
               array[(q[0]-1)+ i] += q[2]
           else:
               array[(q[1]-1)+ i] += q[2]
    return max(array)


def arrayManipulation(n, queries):
        # Big O (N)
        array = [0]*(n+1) # we only really need one terminal row, since we're applying each pass to all rows below

        # loop through all the queries and apply the increments/decrements for each
        # Big O (M) (size of queires)
        for q in queries:
                i, j, k = q[0], q[1], q[2]

                array[i-1] += k # increment the starting position
                # this is where a loop would increment everything else between a & b by k
                # but instead of taking b-a steps, we take a constant 2 steps, saving huge on time
                array[j] -= k # decrement the position AFTER the ending position

        # now loop through res one time - Big O (N) (size of res)
        sm = 0 # running sum
        mx = 0 # maximum value found so far
        for i in range(len(array)):
                sm += array[i]
                if sm > mx:
                        mx = sm

        # total run time is Big O (2*N + M) >> Big O(N)
        return mx
