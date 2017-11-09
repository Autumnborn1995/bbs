import app as bbs

app = bbs.configured_app()

if __name__ == '__main__':
    print('server run')
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=80,
    )
    app.run(**config)
