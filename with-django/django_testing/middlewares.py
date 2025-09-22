import time
from django.db import connection


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


class DatabaseQueryTimeMiddleware:
    """
    Middleware that measures and adds the database query time and count
    to the response headers.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Capture initial query count
        initial_query_count = len(connection.queries)
        
        # Process the request
        response = self.get_response(request)
        
        # Calculate database metrics
        final_query_count = len(connection.queries)
        new_queries = connection.queries[initial_query_count:]
        
        # Sum up the time for all queries executed during this request
        total_db_time = sum(float(query['time']) for query in new_queries) * 1000  # Convert to ms
        query_count = len(new_queries)
        
        # Add headers to response
        response['X-DB-Query-Time'] = f'{total_db_time:.2f}ms'
        response['X-DB-Query-Count'] = str(query_count)
        
        return response
