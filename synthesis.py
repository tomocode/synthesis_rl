# Synthesis Learning Algorithm ver.0.0.5 Developmental Release
# Programmed and Maintained by Tomoyoshi Yamamoto (github@tomocode)

# Please note that this release is a version to demonstrate the algorithm, with no additional features. Therefore,
# this release is limited of its capabilities. Please read README or Projects in GitHub repo site for future
# development.

# import modules
import random

# categories of s
cat = []
# temporalily saves the relation ship between a and s as r
buffer = [0, 0]
# probability of choosing random coefficient (max 1, min 0)
coef = 1
# contain multiple loaf data
memDat = []

actionNode = []


# memory data
class LOAF:
    def _init_(self, pasts, pastr):
        self.s = [pasts]
        self.r = [pastr]


def basicAlg(r, s):
    print("this is Ai algorithm")
    if len(cat) == 0:
        print("make new LOAF data set")
        loafPlaceholder = LOAF(s, r)
        cat.append(loafPlaceholder)

    # pick random or evaluate from statistical evaluation function Ai+1
    evC = random.randint(0, 1)
    if evC >= coef:
        print("evaluation function")
    else:
        # take action randomly
        return actionNode[random.randint(0, len(actionNode))]


def updateCategory():
    print("update category")
