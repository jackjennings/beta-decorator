from beta import beta, BetaObject


class SpeccedObject(BetaObject):

    def foo(self):
        return "foo"

    @beta(foo)
    def foo(self):
        return "beta foo"


class TestBeta(object):

    def test_has_standard_method(self):
        assert SpeccedObject().foo() == "foo"

    def test_has_beta_method(self):
        assert SpeccedObject().beta.foo() == "beta foo"
