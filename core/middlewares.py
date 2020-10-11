import time


def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):


        start = time.time()

        response = get_response(request)

        stop = time.time()

        with open('perf_log.log', 'a+') as f:
            f.write(f'Execution time for {request.method} - {request.path}: {response.status_code}\n')

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware



class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
