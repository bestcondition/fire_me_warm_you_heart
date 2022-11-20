def main():
    from gevent.pywsgi import WSGIServer
    from app import app
    from config import config
    import logging
    
    logging.info(f'{config.to_dict()}')
    
    http_server = WSGIServer(
        (config.HOST, config.PORT),
        app,
    )
    
    http_server.serve_forever()


if __name__ == '__main__':
    main()
