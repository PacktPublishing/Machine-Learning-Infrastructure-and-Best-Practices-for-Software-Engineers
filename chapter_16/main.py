import requests

# URL of the Flask web service for file upload
upload_url = 'http://localhost:5000/success'  # Replace with the actual URL

# URL of the Flask web service for predictions
prediction_url = 'http://localhost:5001/predict/'  # Replace with the actual URL


def upload_file_and_get_metrics(file_path):
    try:
        # Open and read the file
        with open(file_path, 'rb') as file:
            # Create a dictionary to hold the file data
            files = {'file': (file.name, file)}

            # Send a POST request with the file to the upload URL
            response = requests.post(upload_url, files=files)
            response.raise_for_status()

            # Parse the JSON response
            json_result = response.json()
            
            # Extract LOC and mccabe_complexity from the JSON result
            loc = json_result.get('lines_of_code')
            mccabe_complexity = json_result.get('mccabe_complexity')[0][-1]

            if loc is not None and mccabe_complexity is not None:
                print(f'LOC: {loc}, McCabe Complexity: {mccabe_complexity}')
                return loc, mccabe_complexity
            else:
                print('LOC or McCabe Complexity not found in JSON result.')

    except Exception as e:
        print(f'Error: {e}')

def send_metrics_for_prediction(loc, mcc):
    try:
        # Create the URL for making predictions
        predict_url = f'{prediction_url}{loc}/{mcc}'

        # Send a GET request to the prediction web service
        response = requests.get(predict_url)
        response.raise_for_status()

        # Parse the JSON response to get the prediction
        prediction = response.json().get('Defect')

        print(f'Prediction: {prediction}')

    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    # Specify the file path you want to upload
    file_path = './main.py'  # Replace with the actual file path

    # Upload the specified file and get LOC and McCabe Complexity
    loc, mcc = upload_file_and_get_metrics(file_path)

    send_metrics_for_prediction(loc, mcc)
