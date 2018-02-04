#===============================================================================
# Common functions
#===============================================================================

import re
import dropbox



class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)

def saveFile(browser, filePath): 
    content = browser.response.content
    with open(filePath, "wb") as output:
        output.write(content)
    
def uploadToDropbox(fileName):
    print "Upload %s to Dropbox" %fileName
    access_token = 'yourtoken'
    transferData = TransferData(access_token)
    file_path = '/Apps/YourPath/'  # The full path to upload the file to, including the file name
    # API v2
    transferData.upload_file(fileName, file_path + fileName)
    