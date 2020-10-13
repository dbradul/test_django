import copy
from urllib.parse import urlencode

import time


def perf_tracker_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):


        start = time.time()

        response = get_response(request)


        stop = time.time()

        with open('perf_log.log', 'a+') as f:

            elapsed_time = stop - start
            f.write(f'Execution time for {request.method} - {request.path}, {response.status_code}: {elapsed_time}s\n')

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware



class QueryParamsInjectorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        query_params = copy.deepcopy(request.GET)
        if 'page' in query_params:
            del query_params['page']
        request.query_params = urlencode(query_params)

        response = self.get_response(request)

        return response