import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    
    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as a:
            dbx.files_upload(a.read(), file_to)

def main():
    access_token = input("Please enter the generated access token: ")
    transferData = TransferData(access_token)

    file_from = input("Please enter the file name that you want to move to dropbox: ")
    file_to = input("Please enter the file path to upload to dropbox: ")
    #file_from = 'test.txt'
    #file_to = '/test_dropbox/test.txt'

    transferData.upload_file(file_from,file_to)
    print("Your file was moved.")

main()