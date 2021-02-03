def reversal(w):
    replay = w[len(w)- 1]
    for i in range(2, len(w) +1):
        replay = replay + w[len(w) - i]

    return replay

