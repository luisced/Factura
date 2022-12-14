from facturacion import create_app
from flask_admin import Admin
from werkzeug.exceptions import HTTPException
import traceback


app = create_app()
admin = Admin(app)


@app.errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        return e
    print("Error:", traceback.print_exc(), flush=True)
    # now you're handling non-HTTP exceptions only
    return {"error": True, "message": str(e)}, 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True,
            use_reloader=True, use_debugger=True, port=5555)
