# Python FastAPI personal project demos
## Consist of the following
1. <b>URL shortener</b>
2. <b>2FA genrator and validator</b>

## Demonstrates
- Ability to write python backend CRUD operations to a persistent postgres db hosted on aws RDS
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
