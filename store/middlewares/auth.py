from django.shortcuts import redirect

def auth_middleware(get_response):    # it is a decorater
    # One-time configuration and initialization.

    def middleware(request):
        print(request.session.get('user'))
        returnUrl = request.META['PATH_INFO']
        print(request.META['PATH_INFO'])
        if not request.session.get('user'):
            return redirect(f'login?return_url={returnUrl}')
        response = get_response(request)
        return response

    return middleware