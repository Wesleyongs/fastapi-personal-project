# Python FastAPI personal project demos
## Consist of the following
1. URL shortener
- Demonstrates CRUD operations to a persistent postgres db hosted on aws RDS
2. 2FA genrator and validator
- Demonstrates ability to work with APIs (twillio) to build backend services

## Also includes
- CICD pipeline to deploy on aws EC2 after every commit to main branch
- [Demo](http://ec2-18-140-244-94.ap-southeast-1.compute.amazonaws.com/docs)

## Wish to run this locally?
### with make (windows)
```
make venv
```
```
make run 
```

### vanilla python
``` 
python -m venv venv
```
``` 
.\venv\Scripts\activate
```
``` 
venv/Scripts/pip install -r requirements.txt
```
```
python -m src.main 
```

## Screenshots
TBC

## Author
[wesleyongs.com](https:wesleyongs.com)
