from django.shortcuts import redirect

class ForceSingleURLMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path != "/":
            return redirect("/")
        return self.get_response(request)
