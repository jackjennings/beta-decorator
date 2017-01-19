__version__ = "0.0.1"


class BetaDelegator(object):

    def __init__(self, subject):
        self.subject = subject

    def __getattr__(self, key):
        standard = getattr(self.subject, key)

        if hasattr(standard, "_beta"):
            return standard._beta.__get__(self.subject, self.subject.__class__)
        else:
            return standard


class BetaObject(object):

    @property
    def beta(self):
        return BetaDelegator(self)


def beta(base):
    def decorator(new):
        base._beta = new
        return base

    return decorator
