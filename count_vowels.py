def count(string):
    total = 0
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for char in string:
        if char in 'aA':
            a += 1
        if char in 'eE':
            e += 1
        if char in 'iI':
            i += 1
        if char in 'oO':
            o += 1
        if char in 'uU':
            u += 1
        total = a + e + i + o + u
    print ("There are "+ str(a) + " a(s), " + str(e) + " e(s), "+ str(i) + " i(s), " + str(o) + " o(s), and " + str(u) + " (u) for a cumulative total of "+ str(total) + " vowels.")
