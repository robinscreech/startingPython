class Person:

    foo = 'bar'

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def greet(self):
        return "hello there"

    @staticmethod
    def wave():
        return("waving hand")
        # return foo wont work as its static and doesnt have access to class method stuff

    @classmethod
    def say_foo(cls):
        return cls.foo
