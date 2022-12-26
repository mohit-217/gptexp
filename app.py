from inference_gpt import text_generation
from fastapi import FastAPI,File,UploadFile
from parameters import ndaparameters
from face_detect_match import facematch
import shutil
import os
app= FastAPI()

@app.post("/")
def ndaGeneration(data:ndaparameters):
    data = data.dict()
    openai_api_key=data['openai_api_key']
    open_ai_model_name=data['fine_tuned_model_name']
    type_of_nda=data['type_of_nda']
    effective_date=data['effective_date']
    jusdication_of_nda=data['jusdication_of_nda']
    disclosing_party=data['disclosing_party']
    recieving_party=data['recieving_party']
    duration=data['duration']
    obj=text_generation(openai_api_key,open_ai_model_name)
    type_of_nda=data['type_of_nda']
    disclosing_party=data['disclosing_party']
    prompt=f"Generate NDA for {type_of_nda} between disclosing party {disclosing_party} and recieving party:{recieving_party} effective from the date {effective_date} for the Duration: {duration}. NDA should also include provisions based on  Jurisdication {jusdication_of_nda}"
    response=obj.gen_text(prompt)
    print(response)
    return {"Ai Genrated NDA":response}
@app.post("/facematch")
async def facematching(file1: UploadFile=File(...),file2:UploadFile=File(...)):
    if not os.path.exists('temp'):
        os.mkdir('temp')
    file_location1=os.path.join('temp','sample_document.png')
    file_location2=os.path.join('temp','sample_document.png')
    with open(file_location1, "wb") as buffer:
        shutil.copyfileobj(file1.file, buffer)
    file_location1=os.path.join('temp','sample_image.png')
    with open(file_location1, "wb") as buffer:
        shutil.copyfileobj(file2.file, buffer)
    obj=facematch(file_location1,file_location2)
    result=obj.face_match()
    print(result)
    if bool(result[0]):
        return {'face_match_status':"face matched successfully"}
    else:
        return {'face_match_status':"face not matched successfully"}