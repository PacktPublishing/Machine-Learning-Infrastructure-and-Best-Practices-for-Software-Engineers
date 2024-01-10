from fileinput import filename
from flask import *
from radon.complexity import cc_visit
from radon.cli.harvest import CCHarvester

app = Flask(__name__)

# Dictionary to store the metrics for the file submitted
# Metrics: lines of code and McCabe complexity
metrics = {}


def calculate_metrics(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Count lines of code
    lines = len(content.splitlines())

    # Calculate McCabe complexity
    complexity = cc_visit(content)

    # Store the metrics in the dictionary
    metrics[file_path] = {
        'lines_of_code': lines,
        'mccabe_complexity': complexity
    }


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']

        # Save the file to the server
        file_path = f.filename
        f.save(file_path)

        # Calculate metrics for the file
        calculate_metrics(file_path)

        # Return the metrics for the file
        return metrics[file_path]


@app.route('/metrics', methods=['GET'])
def get_metrics():
    if request.method == 'GET':
        return metrics


if __name__ == '__main__':
    app.run(debug=True)
