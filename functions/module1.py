from urllib.request import urlretrieve
import os
import zipfile
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math



class DataHandler:
    
    
    def __init__(self, dataframe = pd.DataFrame()):
        self.dataframe = dataframe

    #Method 1
    def download_file(self,file_link: str, output_file: str):
        """
        Downloads a file from an URL into the /downloads directory on your hard drive.
        
        Parameters
        ------------
        file_link: str
            A string containing the link to the file you wish to download.
        output_file: str
            A string containing the name of the output file. The default value is 'file.zip'
            at the location you are running the function.
            
        Returns
        ---------
        Nothing
        
        
        Example
        ---------
        download_file("https://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip", output_file='data.zip')
        """
    
        # If file doesn't exist, download it. Else, print a warning message.
        if not os.path.exists(f"./downloads/{output_file}"):
            urlretrieve(file_link, filename=f"./downloads/{output_file}")
        else:
            print("File already exists!")
    
    
    #Method 2
    def zip_to_dataframe(self, output_file: str, csv_file: str):
        """
        Creates a pandas dataframe from a csv file inside a specifc zip archive (within your /downloads directory)
        
        Parameters
        ------------
        output_file: str
            A string containing the file name of the zip file you downloaded
        csv_file: str
            A string containing the name of csv file you intend to load into the dataframe
            
        Returns
        ---------
        dataframe head
        
        
        Example
        ---------
        zip_to_dataframe("data.zip", csv_file="day.csv")
        """
        
        zip_contents = zipfile.ZipFile(f"./downloads/{output_file}")
        self.dataframe = pd.read_csv(zip_contents.open(csv_file))
    
    #Method 3
    def plot_correlation_matrix(self):
        """
        Plots a correlation matrix for month, humidity, weather situation,
        temperature, windspeed, and total number of bike rentals
        
        Parameters
        ------------
        None
            
        Returns
        ---------
        seaborn correlation matrix
        """   
        sns.set(rc={'figure.figsize':(15,9)}) 
        sns.heatmap(self.dataframe[["mnth", "weathersit", "temp", "windspeed", "cnt"]].corr(), 
                    annot=True
                    )
        plt.title("Correlation between month, weathersituation, temperature, windspeed and bike rentals", 
                  fontdict={"weight" : "bold",
                            "size" : 20})
    
    #Method 4
    def plot_weekly_data(self, week: int):
        """
        Plots the data of a chosen week 
        
        Parameters
        ------------
        week: int
            A integer for the chosen week which has to be plotted
            
        Returns
        ------------
        Plot of the data of the chosen week
        """
        dates = list(dict.fromkeys(self.dataframe.dteday))

        keys = dates
        x = 0

        weeks = []
        for date in dates:
            x = x + 1/7
            weeks.append(math.floor(x))

        date_week = dict(zip(keys,weeks))
        self.dataframe["week"]= self.dataframe["dteday"].map(date_week)
        
        plt.style.use("seaborn")
        self.dataframe.loc[self.dataframe["week"]==week].plot("instant",
                                                              "cnt", 
                                                              figsize=(15,9))
        plt.title(f"Number of Bike rentals in week {week}", 
                  fontsize=20, 
                  fontweight="bold")
        plt.ylabel("# of bike rentals", fontsize=16)
        plt.xlabel("instant", fontsize=16)
        plt.show()
        