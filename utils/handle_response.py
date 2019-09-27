from flask_restful import abort


def success_response(**kwargs):
    """ Helper function to format and return request success response
    Args(kwargs):
        message: Response Message
        data: Response data payload
        status: Response status code
    """
    return {
        'message': kwargs.get('message', 'Action Successfully Completed'),
        'data': kwargs.get('data'),
        'status': 'success'
    }, kwargs.get('status', 200)


def error_response(**kwargs):
    """ Helper function to format and return request error response
    Args(kwargs):
        message: Response Message
        status: Response status code
    """
    return abort(kwargs.get('status', 400),
                 message=kwargs.get(
                     'message', 'An error has occured'),
                 status='error')
