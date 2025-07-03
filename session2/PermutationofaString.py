def PermutationOfString(s: str) -> list:
    
    if len(s) == 0:
        return ['']
    
    permutations = []
    for i, char in enumerate(s):
        for perm in PermutationOfString(s[:i] + s[i+1:]):
            permutations.append(char + perm)
    
    return permutations
