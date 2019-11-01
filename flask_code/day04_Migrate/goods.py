# from main import app


# @app.route('/get_goods')
def get_goods():
    return 'get goods page'


def route(params):
    def decorator(func):
        def inner():
            pass

        return inner

    return decorator
