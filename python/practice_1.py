a = 'dqwkfoqeksd'
b = tuple(a)
c = list(a)

def test(*lines):
    return lines

test(a,b,c)