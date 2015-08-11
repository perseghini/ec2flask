from flask import request
from flask_templates import app
from functools import wraps

def support_jsonp(f):
    """Wraps JSONified output for JSONP"""

    @wraps(f)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            content = str(callback) + '(' + str(f(*args, **kwargs)) + ')'
            return app.response_class(content,
                                      mimetype='application/javascript')
        else:
            return f(*args, **kwargs)

    return decorated_function
