from webapp import create_app, DevelopmentConfig

app = create_app(configuration=DevelopmentConfig)

if __name__ == '__main__':
  app.run()
