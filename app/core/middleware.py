import time
from fastapi import Request

def audit_middleware(request: Request, call_next):
    start_time = time.time()
    response = call_next(request)
    time_elapsed = time.time() - start_time

    print({
        "path":request.url.path,
        "method":request.method,
        "duration": time_elapsed
    })

    return response
