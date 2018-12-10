from datahub import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='23.226.138.66', debug=True)
