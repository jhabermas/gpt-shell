from hello_world.hello import hello

def test_say_hello():
    assert hello.say_hello("world") == "Hello world"