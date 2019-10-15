# uwsgi reference: https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04

from app import app

if __name__ == "__main__":
    app.run()