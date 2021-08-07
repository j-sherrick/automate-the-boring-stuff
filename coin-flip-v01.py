import random

###########  SET IDENTIFIERS  ###########

SAMPLE_SIZE = 10000
BATCH_SIZE = 100
STREAK_LENGTH = 6
MAX_STREAKS = 10    # The maximum amount of streaks we can reasonably expect to occur in 100 flips.

###########  END IDENTIFIERS  ###########

###########  BEGIN EXPIREMENT ###########

streakTotals = [0] * MAX_STREAKS
 # keeps track of the total number of streaks that occur in each 100 flips.
 # number of streaks corresponds to index of array
 # EX 0 streaks is streakTotals[0], 1 streak is at streakTotals[1], 2 streaks at streakTotals[2]

for expirementNumber in range(SAMPLE_SIZE):
    
    batch = []                  
    # create a new list at the beginning of each expirement for each batch of 100 flips

    streaksInBatch = 0
    # counts the number of times a streak occurs in a batch of 100

    for coinFlip in range(BATCH_SIZE):
        batch.append(random.randint(0, 1))
        # random.randint(0, 1) randomly selects 0 or 1 and appends it to the batch

    streak = 0
    for i in range(1, BATCH_SIZE):
        if(batch[i - 1] == batch[i]):
            streak += 1
            # if the current head or tails (0 or 1) matches the previous, add to our streak counter

            if(streak == STREAK_LENGTH):
                streaksInBatch += 1
                streak = 0
                # if streak counter equals target streak length, add streak to streaksInBatch and reset streak counter

        else:
            streak = 0
            # if heads/tails do not match, reset streak counter
 
    streakTotals[streaksInBatch] += 1
    # Add the total number of streaks in this batch to the streakTotals list

###########  END EXPIREMENT ###########


###########  CALCULATE STREAK PERCENTAGES ###########

percentageByNumber = []
# percentageByNumber holds calculated percentages of streaks by eatch number. 
# For example what % of 100 flips did 0 streaks occur, 1 streak occur, 2 streaks occur, etc...
# Number of streaks, again corresponds to list index i.e. 0 streaks is at percentageByNumber[0], 1 streak at percentageByNumber[1]

percentWithStreaks = 0      # percentWithStreaks will hold the total percantage that had at least one streak
for i in range(MAX_STREAKS):
    percentageByNumber.append(streakTotals[i] / BATCH_SIZE)
    # Calculates the percentages for number of streaks per batch including no streaks, and appends to the appropriate index in the list

    if(i > 0): percentWithStreaks += streakTotals[i]

percentWithStreaks /= BATCH_SIZE    # calculate total percentage that had at least one streak

###########  END CALCULATE STREAK PERCENTAGES ###########


###########  PRINT RESULTS ############

for i in range(MAX_STREAKS):
    print('%s%% of batches contained %d streaks.' % (percentageByNumber[i], i))

print('%s%% of batches contained at least one streak.' % percentWithStreaks)

########## END PRINT RESULTS  ##########