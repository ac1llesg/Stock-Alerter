# Stock Alerter

 Takes real-time stock price and compare it to your target price. 
 Alerts you with a sound when the stock price drops below your target price.
 Updates using Yahoo Finance's price.
 
 
 Use either main.py or main.ipynb to start.
 
 
 ## Requirements
 
Requires playsound, beautiful soup and requests.
 
 
 ## Alerter function usage 
```python
 alerter('webpage', 'target price')
 ```
 
 
 ## Example
```
alerter('https://finance.yahoo.com/quote/FB?p=FB', '160.62') 
# When Facebook drops below 160.62, the alerter will beep once.
```
Lower your volume.


## License
[MIT](https://choosealicense.com/licenses/mit/)
 
