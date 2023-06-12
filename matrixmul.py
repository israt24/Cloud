from flask import Flask


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    # Program to multiply two matrices using nested loops

    # 3x3 matrix
    X = [[7,7,3],
        [4,5,6],
        [1,8,9]]
    # 3x4 matrix
    Y = [[4,8,1,1],
        [4,7,3,0],
        [4,2,9,2]]
    # result is 3x4
    result = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]

    # iterate through rows of X
    for i in range(len(X)):
     # iterate through columns of Y
     for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

    return result


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
