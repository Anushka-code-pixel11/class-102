import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):

        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = "sl.AxQjcMT44v6a_gqTvPeBPLG9GBsL2wfMasnsKLuB-jW0svOnxAGVvZ6Fg6sU661MLYSz5vgz54fhkEnqNlhgEY7h4NI6XMIWvrusWtN0pdksyrnzAYXIiD4V4fbQCUScHYdpKDc"
    transferData = TransferData(access_token)

    file_from = input("Enter the file path :  ")
    file_to = input("Enter the path to upload to dropbox : ")

    transferData.upload_file(file_from, file_to)
    print("File Has Been Moved")

if __name__ == '__main__':
    main()

