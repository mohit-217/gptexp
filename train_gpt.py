import openai
import pandas as pd
import json
model = "text-davinci-002"
epochs = 1
batch_size = 3
state_laws = {
    "Boston": "The Boston Trade Secrets Act",
    "California": "The California Trade Secrets Act"
}
data = []
with open(r"D:\Trato\gptexp\NDA_dataset_prepration\training_data_prepared.jsonl", "r") as f:
    data=json.loads(f)
df=pd.read_csv(r'D:\Trato\gptexp\NDA_dataset_prepration\training_data.csv')
# Create a list of input prompts and corresponding output texts
prompts = [nda for nda in df['prompt']]
output_texts = [nda for nda in df['ouput']]
response = openai.Completion.create(
    engine=model,
    prompt=prompts,
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=1,
    presence_penalty=1,
    best_of=1,
    stop=None,
    n=1,
    stream=False,
    temperature_annealing_schedule=None,
    max_tokens_per_batch=1024,
    training_data=output_texts,
    training_batch_size=batch_size,
    training_epochs=epochs,
    training_accumulation_steps=1,
    training_strategy="all_at_once",
    training_optimizer="sgd",
    training_optimizer_lr=0.001,
    training_optimizer_momentum=0.9,
    training_optimizer_beta1=0.9,
    training_optimizer_beta2=0.999,
    training_optimizer_epsilon=1e-8,
    training_optimizer_weight_decay=0.01,
    training_optimizer_amsgrad=False,
    training_max_grad_norm=1.0,
)

# Print the training results
print("Training complete!")
print("Total training time:", response["training_elapsed_time"], "seconds")
print("Training loss:", response["training_loss"])