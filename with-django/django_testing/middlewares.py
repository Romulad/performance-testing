import time

class ProcessingTimeMiddleware:
    """
    Middleware that measures and adds the total request processing time 
    (in milliseconds) to the response headers.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        total_start = time.perf_counter()
        response = self.get_response(request)
        total_elapsed = (time.perf_counter() - total_start) * 1000  # ms
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
        view_start = time.perf_counter()
        response = self.get_response(request)
        view_elapsed = (time.perf_counter() - view_start) * 1000  # ms
        response['X-View-Processing-Time'] = f'{view_elapsed:.2f}ms'
        return response
