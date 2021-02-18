from urllib.request import urlretrieve
import os
import zipfile
import pandas as pd


class DataHandler:
    def __init__(self,file_link, output_file, csv_file):
        self.file_link = file_link
        self.output_file = output_file
        self.csv_file = csv_file

    #Module 1
    def download_file(file_link: str, output_file: str='file.zip'):
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
    
    
    #Module 2
    def zip_to_dataframe(output_file: str, csv_file: str):
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
        zip_to_dataframe("data.zip", csv_file="day.csv", dataframe_name="daydf")
        """
        
        zip_contents = zipfile.ZipFile(f"./downloads/{output_file}")
        df = pd.read_csv(zip_contents.open(csv_file))
        return df.head()
        
    