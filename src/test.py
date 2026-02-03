class Hello:
    name = "youssef"

    def __init__(self):
        last_name = "youssef"
    @classmethod
    def set_name(cls, name):
        cls.name = name


person = Hello()
person.set_name("ahmed")
print(Hello.name)

