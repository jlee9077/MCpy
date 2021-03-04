# MCpy
Monte Carlo Simulator for Options and stock data visualizer

## Getting Started

Python packages installed in a virtual environment. To activate your virtual environment run the following:

```
source venv/bin/activate
```

## Guide

For testing the Monte Carlo Option simulator, run the following command:

```
pythonw monte_carlo.py
```

You should see the following simulations:


<img width=50% alt="distribution" src="https://user-images.githubusercontent.com/38798668/97263960-59c0c300-17fa-11eb-9543-3fddbca430c9.png">

<img width=50% alt="gaussian" src="https://user-images.githubusercontent.com/38798668/97263984-63e2c180-17fa-11eb-81e9-c1078a15bb82.png">

<img width=50% alt="histogram" src="https://user-images.githubusercontent.com/38798668/97263909-431a6c00-17fa-11eb-98a1-652b7f4c728f.png">

For testing out the stock data visualizer, run the following command:

```
python stock_data.py
```

When running the above command, you will see the following in your terminal:

```
Please Enter Ticker Symbol:
```

When prompted, enter a valid ticker symbol such as `PLTR` or `GME`. It should show the following below:

```
('You entered ticker : ', 'PLTR')
```

The following graph will render in your browser:

<img width=70% alt="histogram" src="https://user-images.githubusercontent.com/38798668/99498482-870a1800-2945-11eb-96e2-a783a1ab151b.gif">
