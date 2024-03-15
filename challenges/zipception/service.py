from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Index page with login and signup links
@app.route('/')
def index():
    return render_template('index.html')

# endpoint to download encrypted flag
@app.route('/download_goldnugget_zip')
def download_output():
    return send_from_directory('.', 'goldnugget.zip', as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
