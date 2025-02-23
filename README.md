![ML API Overview](images/bniladridas-ml-api.png)

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-green?logo=fastapi)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-orange?logo=huggingface)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red?logo=pytorch)

# ml-api

A machine learning API for model deployment and inference.

## Overview
ml-api is a RESTful API designed for deploying and serving machine learning models. It allows users to easily upload models, generate predictions, and manage model versions.

[View Interactive Project Overview](project_overview.html)

## Deployment
To deploy the web interface:
```bash
kubectl apply -f html_deployment.yaml
```

## Features
- Model upload
- Real-time inference
- Model version management

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/bniladridas/ml-api.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ml-api
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Requirements
- Python 3.x
- Flask (or any other relevant packages)

## Usage
To start the API server, run:
```bash
python main.py
```
### Example Request
```bash
curl -X POST http://localhost:5000/predict -d '{"data": [your_data_here]}'
```

## Contributing
Feel free to submit issues or pull requests for improvements!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
