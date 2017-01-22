==============
Beta Decorator
==============

This package provides a proof of concept for providing an alternate implementation of a class method.

Example
=======

Implementation in progress. Should do something like this:

.. code-block:: python

  from beta import beta, BetaObject

  class SpeccedObject(BetaObject):

      def foo(self):
          return "foo"

      @beta(foo)
      def foo(self):
          return "beta foo"
