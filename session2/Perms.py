def PermutationString (s):
    
    if len(s) == 0:
        return ""
    permutations = []
    # to assign numerivalue to each char except spaces  
    for i,char in enumerate(s):
         for perm in PermutationString(s[:i] + s[i+1:]):
            PermutationString.append(char + perm)
    return permutations    