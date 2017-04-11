def z_function_trivial(s):
    n = len(s)
    z = [0]*n
    i = 1
    while i < n:
        while i + z[i] < n and s[z[i]] == s[i+z[i]]:
            z[i] += 1
        i += 1
    return z

def z_function(s):
    z = [0]*len(s)
    left = right = 0
    for i in range(1, len(s)):
        x = min(z[i-left], right-i+1) if i <= right else 0
        while i+x < len(s) and s[x] == s[i+x]:
            x += 1
        if i + x - 1 > right:
            left, right = i, i + x - 1
        z[i] = x
    return z

print(z_function_trivial('abacaba'))
print(z_function('abacaba'))