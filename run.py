from webapp import create_app
from webapp.config import DevelopmentConfig

app = create_app(configuration=DevelopmentConfig)

if __name__ == '__main__':
  app.run()
