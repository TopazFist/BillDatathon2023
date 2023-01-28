"""
Calculates the lavenshtein distance between two strings.
It will find the minimum number of total insertions/deletions/edits
to get from one string to another.

Uses a dynamic programming algorithm and can penalize insertions,
deletions, and edits differently

Credit to GeeksForGeeks.org for this algorithm that I modified
"""
def lavenshtein(str1, str2, p_insert=1, p_delete=1, p_edit=1):
    # Create a table to store results of subproblems
    dp = [[0 for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
 
    # Fill d[][] in bottom up manner
    for i in range(len(str1) + 1):
        for j in range(len(str2) + 1):
 
            # If first string is empty, only option is to
            # insert all characters of second string
            if i == 0:
                dp[i][j] = j    # Min. operations = j
 
            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i    # Min. operations = i
 
            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
 
            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = min(dp[i][j-1] + p_insert,        # Insert
                                   dp[i-1][j] + p_delete,        # Remove
                                   dp[i-1][j-1] + p_edit)    # Replace
 
    return dp[-1][-1]

print(lavenshtein("cowbell", "cowell"))