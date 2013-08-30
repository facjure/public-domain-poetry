import pystache

def hello_world(text):
    return "Hello %s from Frozen Pie" % text

def all_posts(text):
    renderer = pystache.Renderer(file_encoding="utf-8", string_encoding="utf-8")
    return renderer.render(text, {"posts": contents })
