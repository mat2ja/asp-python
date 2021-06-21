# Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used for index −n ≤ k < 0,
# what is the equivalent index j ≥ 0 such that s[j] references the same element?

a = ['matija', 'jede', 'samo', 'integralno', 'brasno']
n = len(a)
print(a[0], a[-n])
print(a[1], a[-4])
print(a[2], a[-3])
print(a[3], a[-2])
print(a[4], a[-1])
