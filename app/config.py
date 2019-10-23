class Base(object):
    APP_NAME = 'Duck_API_Server'
    TESTING = True
    DEBUG = True
    DATABASE_NAME = 'NONE'


class DevelopmentConfig(Base):
    DEBUG = True
    TESTING = True
    PORT = 8000
    SERVER_HOST = '127.0.0.1'
    DATABASE_NAME = 'duckdevdb'
    CLIENT_HOST = 'https://localhost:3000'
    PRIVATE_KEY_PEM = '/Users/mac/WebstormProjects/TeamProject/duckhoogosa/duckhoogosa-server-kth/cert/key.pem'
    CERT_PEM = '/Users/mac/WebstormProjects/TeamProject/duckhoogosa/duckhoogosa-server-kth/cert/cert.pem'


class TestConfig(Base):
    DEBUG = True
    TESTING = True
    PORT = 7999
    SERVER_HOST = '172.31.32.164'
    DATABASE_NAME = 'ducktestdb'
    CLIENT_HOST = 'https://test.duckhoo.site'
    PRIVATE_KEY_PEM = '/etc/letsencrypt/live/infra.duckhoo.site/privkey.pem'
    CERT_PEM = '/etc/letsencrypt/live/infra.duckhoo.site/cert.pem'


class ProductionConfig(Base):
    DEBUG = True
    PORT = 8000
    SERVER_HOST = '172.31.32.164'
    DATABASE_NAME = 'duckproductiondb'
    CLIENT_HOST = 'http://duckhoo.site'
    PRIVATE_KEY_PEM = '/etc/letsencrypt/live/infra.duckhoo.site/privkey.pem'
    CERT_PEM = '/etc/letsencrypt/live/infra.duckhoo.site/cert.pem'
