words = "I wish I may I wish I might".split()
def buildtrigrams(words):
    trigrams = {}
    for i in range(len(words) - 2):
        pair = tuple(words[i:i + 2])
        followerlist = [words[i + 2]]
        follower = words[i + 2]
        if pair in trigrams:
            trigrams[pair].append(follower)
        elif pair not in trigrams:
            trigrams.setdefault(pair, followerlist)
    return trigrams

if __name__ == "__main__":
    trigrams = buildtrigrams(words)
    print(buildtrigrams(words))
    # print("keys are {}".format(trigrams.keys()))
    # print("values are {}".format(trigrams.values()))




#Take1
# words = "I wish I may I wish I might I wish I may I wish I might".split()
# def buildtrigrams(words):
#     trigrams = {}
#     for i in range(len(words) - 2):
#         pair = tuple(words[i:i + 2])
#         follower = [words[i + 2]]
#         print(type(follower))
#         trigrams.setdefault(pair, follower)
#     return trigrams
#
# if __name__ == "__main__":
#     trigrams = buildtrigrams(words)
#     print(buildtrigrams(words))
#     # print("keys are {}".format(trigrams.keys()))
#     # print("values are {}".format(trigrams.values()))

#Take2
# words = "I wish I may I wish I might".split()
# def buildtrigrams(words):
#     trigrams = {}
#     for i in range(len(words) - 2):
#         pair = tuple(words[i:i + 2])
#         follower = [words[i + 2]]
#         trigrams.setdefault(pair, follower)
#         trigrams[pair].append(follower)
#     return trigrams
