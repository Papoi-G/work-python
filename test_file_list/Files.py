class Files:
    
    def __init__(self, fileId) -> None:
        self.fileId = fileId

    def get_size(self,fileId):
        file = self.drive_service.files().get(fileId, fields='size,modifiedTime').execute()


