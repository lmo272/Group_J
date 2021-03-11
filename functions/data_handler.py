"""
This module contains the DataHandler class, which
performs data imports and basic plotting.
Classes:
    DataHandler
Functions:
    download_file
    zip_to_dataframe
    plot_correlation_matrix
    plot_weekly_data
    plot_monthly_average
    forecast
"""

import math
import os
import zipfile
from urllib.request import urlretrieve
from dataenforce import Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime



class DataHandler:
    """
    A class to hold data and perform basic exploratory data operations.
    Attributes:
    -----------
    dataframe: Dataset
      A DataFrame containing the downloaded data
    Methods:
    -----------
    download_file(file_link: str, output_file: str):
      Downloads the specified output file contained in
      file_link into the "downloads" directory.
    zip_to_dataframe(output_file: str, csv_file: str):
      Creates a pandas dataframe from a csv file inside
      a specific zip archive (within your /downloads directory).
    plot_correlation_matrix(self):
      Plots a correlation matrix for month, humidity, weather situation,
        temperature, windspeed, and total number of bike rentals
    plot_weekly_data(week: int):
      Plots the data of a chosen week
    plot_monthly_average(self):
        Plots the average total rentals by month of the year
    forecast(self, month: int):
        Plots the bike rental forecast for a 168-hour period (a Mon-Sun week)
        corresponding to the average rental with a shaded area corresponding to an interval of [-1 std deviation, +1 std deviation.].
    """

    def __init__(self, dataframe: Dataset = pd.DataFrame()):
        self.dataframe = dataframe

    # Method 1
    @staticmethod
    def download_file(file_link: str, output_file: str):
        """
        Downloads a file from an URL into the /downloads directory
        on your hard drive.
        Parameters
        ------------
        file_link: str
            A string containing the link to the file you wish to download.
        output_file: str
            A string containing the name of the output file.
            The default value is 'file.zip' at the location
            where you are running the function.
        Returns
        ---------
        Nothing
        Example
        ---------
        download_file("https://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip",
        output_file='Bike-Sharing-Dataset.zip')
        """

        # If file doesn't exist, download it. Else, print a warning message.
        if not os.path.exists(f"./downloads/{output_file}"):
            urlretrieve(file_link, filename=f"./downloads/{output_file}")
        else:
            print("File already exists!")

    # Method 2
    def zip_to_dataframe(self, output_file: str, csv_file: str):
        """
        Creates a pandas dataframe from a csv file with daily datetime as index
        inside a specific zip archive (within your /downloads directory)
        Parameters
        ------------
        output_file: str
            A string containing the file name of the zip file you downloaded
        csv_file: str
            A string containing the name of csv file you intend
            to load into the dataframe
        Returns
        ---------
        Nothing
        Example
        ---------
        zip_to_dataframe("data.zip", csv_file="day.csv")
        """
        zip_contents = zipfile.ZipFile(f"./downloads/{output_file}")
        # Stores unzipped DataFrame as instance attribute "dataframe".
        self.dataframe = pd.read_csv(zip_contents.open(csv_file))
        self.dataframe.dteday = pd.to_datetime(self.dataframe.dteday)
        self.dataframe = self.dataframe.set_index("dteday")
        self.dataframe.index +=  pd.to_timedelta( self.dataframe.hr, unit='h')
        
    # Method 3
    def plot_correlation_matrix(self):
        """
        Plots a correlation matrix for month, humidity, weather situation,
        temperature, windspeed, and total number of bike rentals
        Returns
        ---------
        Seaborn correlation matrix
        """
        sns.heatmap(
            self.dataframe[["mnth", "weathersit", "temp", "windspeed", "cnt"]].corr(), annot=True
        )
        plt.title("Correlation between month, weathersituation, temperature, windspeed and bike rentals", 
                  fontdict={"weight" : "bold",
                            "size" : 20})
    
    # Method 4
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
        if week > 102 or week < 0:
            raise ValueError("""Specified week outside of allowed range.
                             Week must be integer between 0 and 102.""")

        dates = list(dict.fromkeys(self.dataframe.index))

        keys = dates
        counter = 0

        weeks = []
        for _ in dates:
            counter = counter + 1 / 7
            weeks.append(math.floor(counter))

        date_week = dict(zip(keys, weeks))
        self.dataframe["week"] = self.dataframe.index.map(date_week)

        plt.style.use("seaborn")
        self.dataframe.loc[self.dataframe["week"] == week].\
            plot("instant", "cnt", figsize=(15, 9))
        plt.title(f"Number of Bike rentals in week {week}",
                  fontsize=20, fontweight="bold")
        plt.ylabel("# of bike rentals", fontsize=16)
        plt.xlabel("instant", fontsize=16)
        plt.show()
           
    #Method 5
    def plot_monthly_average(self):
        """
        Plots the average total rentals by month of the year
        Parameters
        ------------
        None
        Returns
        ------------
        Vertical Barchart with the average total rentals by month of the year
        Example
        ------------
        plot_monthly_average()
        """
        plt.style.use("seaborn")
        plt.bar(x=range(1,13), 
                height=self.dataframe.groupby(self.dataframe.index.month).sum("cnt")["cnt"].values*0.5)
        plt.title("Average total rentals by month of the year",
                   fontsize=20, fontweight="bold")
        plt.ylabel("# of bike rentals", fontsize=16)
        plt.xlabel("month", fontsize=16)
        plt.show()
        
    #Method 6
    def forecast(self, month: int):
        """
        Plots the bike rental forecast for a 168-hour period (a Mon-Sun week) as a blue line
        and the rental forecast [-1 std deviation, +1 std deviation.], shown in the shaded area.
                
        Parameters
        ------------
        month: int
            A integer between 1-12 inclusive, representing the months of a year (January-December)
        df_month
        
        Returns
        ---------
        A plot with two visual elements. The plot has a 168h period on the x-axis and the number of bikes rented
        on the y-axis
        The first visual element is the blue line, showing the expected rentals for that week based on the average rentals of the two years in the dataset.
        The second visual elements is the gray shayed area, representing the expected rental for the week
        +and- one standart deviation.
        Example
        ---------
        forecast(3)
        """
        df_month = self.dataframe.loc[self.dataframe.index.month == month]
        df_month = df_month.groupby(["weekday","hr"]).cnt.agg(["mean", "std"])
        df_month.index = df_month.index.get_level_values(1)
        df_month = df_month.reset_index()
        fig, ax = plt.subplots(figsize=(15,9))

        datetime_object = datetime.datetime.strptime(str(month), "%m")
        full_month_name = datetime_object.strftime("%B")

        ax.fill_between(df_month.index,
                        df_month['mean']-df_month['std'],
                        df_month['mean']+df_month['std'],
                        alpha=0.4)

        df_month['mean'].plot(ax=ax)

        ax.set_ylabel("# of bike rentals", fontsize=16)
        ax.set_xlabel("hour", fontsize=16)

        plt.title(f"Expected weekly rentals in {full_month_name}",
                  fontsize=20, fontweight="bold")
        plt.show()