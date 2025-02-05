from google.appengine.runtime import request_environment as request_environment

BACKGROUND_REQUEST_ID: str

class _BackgroundRequest:
    def __init__(self) -> None: ...
    def ProvideCallable(self, target, args, kwargs): ...
    def WaitForCallable(self): ...

class _BackgroundRequestsContainer:
    def __init__(self) -> None: ...
    def EnqueueBackgroundThread(self, request_id, target, args, kwargs): ...
    def RunBackgroundThread(self, request_id) -> None: ...

def EnqueueBackgroundThread(request_id, target, args, kwargs): ...
def Handle(environ): ...
def App(environ, start_response) -> None: ...
