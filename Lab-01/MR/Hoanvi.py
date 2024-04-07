def permutations(lst):
    if len(lst) <= 1:
        return [lst]
    else:
        perms = []
        for perm in permutations(lst[1:]):
            for i in range(len(lst)):
                perms.append(perm[:i] + [lst[0]] + perm[i:])
        return perms

input_list = [1, 2, 3]
all_perms = permutations(input_list)

for perm in all_perms:
    print(perm)
