from pydantic import BaseModel
class ndaparameters(BaseModel):
    type_of_nda:str
    information_needs_protection:str
    jusdication_of_nda:str
    disclosing_party:str
    recieving_party:str
    duration:int