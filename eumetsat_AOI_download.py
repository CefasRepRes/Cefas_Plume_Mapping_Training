# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 2022 @ 07:40:01 2022

@authors: Lenka Fronkova, Richard Harrod, the original comes from EUMETSAT
"""
import eumdac
import datetime
import shutil
import os
import csv
import pandas as pd

from datetime import date, timedelta

""""This function creates a time range from start date and end date and is used
to tun the download function below:
start_date = start date in a format (YYYY, M, D), e.g. date( 2020, 8, 1) 

end_date = end date in a format (YYYY, M, D), e.g. date( 2020, 12, 31)
"""

#function to create the dates
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)
        
""""This function downloads data using EUMETSAT API using the eumdac library
year = year (integer), 
month = month (integer),
day = day (integer) 
login_credentials = a csv document with the user's conusmer key and secret from the Eumetsat Data Store, 
product_id = product ID that will be donwloaded (this needs to be known ahead otherwise use this code
                                                 to explore the products: https://github.com/CefasRepRes/Cefas_Plume_Mapping_Training/blob/main/Eumetsat_Download_General.ipynb), 
east = east bound (integer), 
south = south bound(integer), 
west = west bound (integer), 
north = north bound (integer)

"""

def download(year, month, day, login_credentials, product_id, east, south, west, north, outPath, csv_file):
    login = pd.read_csv(login_credentials)
    
    consumer_key = login["consumer_key"][0] # consumer key
    consumer_secret = login["consumer_secret"][0] #consumer secret

    credentials = (consumer_key, consumer_secret)

    token = eumdac.AccessToken(credentials)

    print(f"This token '{token}' expires {token.expiration}")

    # Get all collection you can explore
    datastore = eumdac.DataStore(token)

    # Select a collection
    selected_collection = datastore.get_collection(product_id)
    
    ### Filter products of selected collection by time and area:###
    
    #Add vertices for polygon, wrapping back to the start point.
    geometry = [[east, south],
                 [east, north],
                 [west, north],
                 [west, south],
                 [east, south]]
     
    # Set sensing start and end time
    # year, month, day, hour, minute
    # e.g., 2021-11-10 08:00:00
    start = datetime.datetime(year, month, day, 1, 0)
    end = datetime.datetime(year, month, day, 23, 59)
    
    # Retrieve datasets that match the selected filter
    products = selected_collection.search(
        geo='POLYGON(({}))'.format(','.join(["{} {}".format(*coord) for coord in geometry])),
        dtstart=start, 
        dtend=end)
      
    print(f'Found Datasets: {len(products)} datasets for the given time range')
    
    #define the output folder based on your time selection
    out_folder = outPath+str(year)+"/"+str(month)+"/"
    
    
    for product in products:
        try:
            print("Start: " + str(product))
            with product.open() as source:
                out_file = os.path.join(out_folder,str(product) + ".zip")
                print(out_file)
                dest_file = open(out_file,'wb')
    
                shutil.copyfileobj(source,dest_file) 
                print(f'Download of product {product} finished.')
        except ValueError:
             #write the source of the layers which had a different value here
                csv_file = open(csv_file, "a+", newline="")
                
                #writing the data into the file
                with csv_file:
                    write = csv.writer(csv_file)
                    write.writerows([[product]])
                print("Download failed for: ")
                print(product)
                pass
        except TimeoutError:
             #write the source of the layers which had a different value here
                csv_file = open(csv_file, "a+", newline="")
                
                #writing the data into the file
                with csv_file:
                    write = csv.writer(csv_file)
                    write.writerows([[product]])
                print("Download failed for: ")
                print(product)
                pass

###################run the functions########################################## 

# set start and end date
# warning the final date is the day before the end_date
start_date = date(2019, 12, 16)
end_date = date(2020, 1, 1) # the end date needs to be the end date +1

####loop through the time range on daily basis
for single_date in daterange(start_date, end_date):
    print(single_date.strftime("%Y%m%d"))
    
    year = int(single_date.strftime("%Y"))
    month = int(single_date.strftime("%m"))
    day = int(single_date.strftime("%d"))
    
    download(year = year, 
             month = month, 
             day = day, 
             login_credentials = "yourPath/data_store_login.csv", 
             product_id = "EO:EUM:DAT:0556",  #define the product ID
             east = 75, 
             south =2.5, 
             west =99, 
             north =24, 
             outPath ="outputPath",
             csv_file = r"yourPath/download_error.csv") #define csv file for error handling cathes
    
 
    
    
    
    

   
        