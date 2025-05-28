# ml-api  
Build, deploy, and scale machine learning with ease.  

## Craft Intelligence  
ml-api is a sleek, RESTful API for deploying and serving machine learning models. Upload models, generate real-time predictions, and manage versions seamlessly.  


## Features  
- **Upload Models**: Deploy your models effortlessly.  
- **Real-Time Inference**: Generate predictions instantly.  
- **Version Management**: Keep your models organized and up to date.  

## Get Started  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/bniladridas/ml-api.git  
   ```  
2. Navigate to the project:  
   ```bash  
   cd ml-api  
   ```  
3. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

## Deploy the Web Interface  
```bash  
kubectl apply -f k8s.yaml
```  

## Run the API  
Launch the server with:  
```bash  
python main.py  
```  

### Example Request  
```bash  
curl -X POST http://localhost:5000/predict -d '{"data": [your_data_here]}'  
```  

## Requirements  
- Python 3.8+  
- FastAPI, HuggingFace Transformers, PyTorch  

## Contribute  
Shape the future of ml-api. Submit issues or pull requests to make it even better.  

## License  
Licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
