def get_bemi_context(request):
    return {
        'user_id': request.user.id if request.user.is_authenticated else None,
        'method': request.method,
        'path': request.path,
    }