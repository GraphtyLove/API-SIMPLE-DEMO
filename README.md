# API-SIMPLE-DEMO

## Folder architecture
-
-- README.md
-- App.py

-- Training
---- training.py

-- Models
---- Model.pickle


## Application features
### Routes
- `/` -> alive 
- `/train` -> Train the model and save it
- `/predict` -> Return a prediction



## Docker informations
### Build
```bash
docker build -t api-demo .
```
### Run
```bash
docker run -v $PWD:/app -p 5000:5000 -it api-demo bash
```

### VScode extension
- `Remote container`