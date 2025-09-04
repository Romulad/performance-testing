import time


def performance_timer(get_response, request):
    start = time.perf_counter()
    response = get_response(request)
    elapsed = (time.perf_counter() - start) * 1000  # ms
    return response, elapsed


class ProcessingTimeMiddleware:
    """
    Middleware that measures and adds the total request processing time 
    (in milliseconds) to the response headers.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response, total_elapsed = performance_timer(self.get_response, request)
        response['X-Total-Processing-Time'] = f'{total_elapsed:.2f}ms'
        return response


class ViewProcessingTimeMiddleware:
    """
    Middleware that measures and adds the view processing time to the 
    response headers.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response, view_elapsed = performance_timer(self.get_response, request)
        response['X-View-Processing-Time'] = f'{view_elapsed:.2f}ms'
        return response
