from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <html>
            <head><title>Run Python Script</title></head>
            <body>
                <h1>Run Your Python Script</h1>
                <form method="POST" action="/run-script">
                    <button type="submit">Run</button>
                </form>
            </body>
        </html>
    '''

@app.route('/run-script', methods=['POST'])
def run_script():
    try:
        # Replace 'your_script.py' with the path to your Python script
        subprocess.run(["python", "C:/Users/05444/Downloads/Working shikhar.txt"], check=True)
        return "Script executed successfully!"
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(host='172.25.23.138', port=5000)
