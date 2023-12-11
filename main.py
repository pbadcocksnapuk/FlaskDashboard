from website import create_app

app = create_app()

# won't execute when we import the file
if __name__ == '__main__':
    app.run(debug=True)
