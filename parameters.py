from pydantic import BaseModel
class ndaparameters(BaseModel):
    openai_api_key:str
    fine_tuned_model_name:str
    type_of_nda:str
    jusdication_of_nda:str
    disclosing_party:str
    recieving_party:str
    duration:int
class facematchpath(BaseModel):
    sampledocument=str
    referenceimage=str