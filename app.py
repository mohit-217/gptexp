from exp import text_generation
from fastapi import FastAPI
from parameters import ndaparameters
app= FastAPI()

@app.post("/")
def ndaGeneration(data:ndaparameters):
    data = data.dict()
    openai_api_key=data['openai_api_key']
    type_of_nda=data['type_of_nda']
    information_needs_protection=data['information_needs_protection']
    jusdication_of_nda=data['jusdication_of_nda']
    disclosing_party=data['disclosing_party']
    recieving_party=data['recieving_party']
    duration=data['duration']
    obj=text_generation(openai_api_key)
    type_of_nda=data['type_of_nda']
    disclosing_party=data['disclosing_party']
    prompt=f"\nType of NDA: {type_of_nda}\nInformation need protection:{information_needs_protection}\nJurisdication for NDA: {jusdication_of_nda}\nNo of parties: 2\ndisclosing party:{disclosing_party}\nrecieving party:{recieving_party}\nDuration: {duration}\n\nQ. Write NDA from above information."
    response=obj.gen_text(prompt)
    print(response)
    return {"Ai Genrated NDA":response}