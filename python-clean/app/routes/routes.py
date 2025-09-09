from fastapi import APIRouter,UploadFile,File

router = APIRouter(prefix='/file',tags=['files'])

def moduleRouter():
    
    router.post('/')
    async def upload_csv(file:UploadFile = File(...)):
        return
    
    router.get('/historical')
    def get_historical():
        return
    
    return router