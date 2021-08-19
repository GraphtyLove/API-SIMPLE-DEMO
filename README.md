# API-SIMPLE-DEMO

Simple API that train and predict on a model for [Iris dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html).

## In production
https://api-demo-becode.herokuapp.com/

## Folder architecture
```
-
-- README.md
-- App.py
-- Training
---- training.py
-- Models
---- Model.pickle
```

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
With volumes:

```bash
docker run -v $PWD:/app -p 5000:5000 -it api-demo bash
```

Without:
```bash
docker run -p 5000:5000 -it api-demo bash
```

Without interactive mode:
```bash
docker run -p 5000:5000 -t api-demo
```

### VScode extension
- `Remote container`
- `Docker`