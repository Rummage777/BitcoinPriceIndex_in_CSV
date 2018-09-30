# BitcoinPriceIndex_in_CSV

Get Bitcoin Price Index from coindesk.com using CoinDesk API  and save results in CSV file


## REQUIREMENTS: 
- python 3.5.x or later
- requests library 

To install Requests type in command line: 
```
pip3 install requests
```

## DESCRIPTION:

As a result you'll have an CSV file with Bitcoin price in USD from CoinDesk.com web-site. 

By default program will create a CSV file for default period (since 01-01-2018 to 21-09-2018).

To start a program, you should open Terminal and choose directory with a projects files.
In your command line type: 
```
python3 main.py
```

Your CSV file will be saved in a current directory.


#### OPTIONS:

Use optional parameters to set your own period:
```
-s, --start              Set a start date in YYYY-MM-DD format
-e, --end                Set a end date in YYYY-MM-DD format
```

Parameters must be listed as a pair of start and end parameters, with dates supplied 
in the YYYY-MM-DD format

Exapmle: to get BPI since 01-09-2018 to 10-09-2018 type in 
command line: 
```
python3 main.py -s 2018-09-01 -e 2018-09-10
```

**Additional parameters:**
```
-h, --help               For getting more help
-n, --name               Set name for output csv file. Default name "bpi.csv"
```

Example: if you want set name "Result" for your output csv file in your command line type: 
```
python3 main.py -n Result
```
Extension csv will be added to chosen name automatically.
