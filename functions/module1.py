from urllib.request import urlretrieve
import os
import zipfile
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class DataHandler:
    
    
    def __init__(self):
        self.data_frame = []

    #Method 1
    def download_file(file_link: str, output_file: str):
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
        download_file("https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip", output_file='student.zip')
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
        data_frame = pd.read_csv(zip_contents.open(csv_file))
        self.data_frame = data_frame
    
    #Method 3
    def plot_correlation_matrix(data_frame: str):
        """
        Plots a correlation matrix for month, humidity, weather situation,
        temperature, windspeed, and total number of bike rentals
        
        Parameters
        ------------
        dataframe: str
            A string containing the name the pandas dataframe, which should be plotted
            
        Returns
        ---------
        seaborn correlation matrix
        """    
        sns.heatmap(data_frame[["mnth", "weathersit", "temp", "windspeed", "cnt"]].corr())
    
    #Method 4
    def plot_weekly_data(week: int):
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
        plt.show()