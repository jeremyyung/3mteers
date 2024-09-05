from flask import Flask, request, render_template
app = Flask(__name__)

#Return static page
@app.route('/')
def run():
    client_ipaddr = request.remote_addr
    return render_template('static.html', client_ip=client_ipaddr)

# run the application
if __name__ == "__main__":
    PORT = 8080
    app.config['DEBUG'] = False
    app.run(host='0.0.0.0', port=PORT)