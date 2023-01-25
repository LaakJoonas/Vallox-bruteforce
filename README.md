# Vallox-bruteforce
Did you forget your Vallox Home PIN for your air conditioner? Try this.

You will need selenium installed. To install, use ```pip install selenium```
To run the app use ```python lmfao.py [IP of Vallox device with http:// before the IP]```
For example ```python lmfao.py http://123.456.789.10```

Make sure to be in the same network as the Vallox Home device. This application might take a while to find the correct pin. Unfortunately Vallox Home requires Javascript to work and thus the app has to use selenium and have the overhead of having to wait for CSS to update.
