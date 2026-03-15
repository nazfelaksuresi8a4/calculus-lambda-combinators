'''lambda calculus computer science theory'''

def Y(le):
    def _inner(cc):
        return le(lambda x : cc(cc)(x))
    return _inner(_inner)

fx = Y(lambda x : x)
fx(fx)(fx)
