# importing the required modules
import os
import shutil
import time
from typing import Counter

# main function
def main():

    #installing time count
    deleted_folder_count = 0
    deleted_files_count = 0

    #specify the path
    path = "/PATH_TO_DELETE"

    #specify the days
    days = 30

    #converting days to seconds
    # time.time() returns current time in seconds
    seconds = time.time() - (days * 24 * 60 * 60)


    #checking wether the files is present i path or not
    if os.path.exists(path):

        #literating over each and every folder and file in gthe path
        for root_folder, folders, files in os.walk(path):

            #comparing the days
            if seconds >=get_file_or_folder_age(root_folder):

                #removing the folder
                remove_folder(root_folder)
                deleted_folder_count += 1 = #incrementing count

                #breaking after removing the root_folder
                break

            else:

                #checking folder from the rooot_folder
                for folder in folders:

                    # folder path
                    folder_path = os.path.join(root_folder, folder)

                    #comparing with the days
                    if seconds >=get_file_or_folder_age(folder_path):

                        #invoking the remove_folder function
                        remove_folder(folder_path)
                        deleted-folders_count += 1 #incrementing count

                           #checking the current directory files
                           for file in files:

                               #file path
                               file_path = os.path..join(root_folder, file)


                               # comparing the days 
                               if seconds >= get_file_or_folder_age(path):                   