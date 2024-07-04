import pandas as pd
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, TextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments

# Cargar el dataframe
df = pd.read_csv('df_electric_cars.csv')

# Crear texto de entrenamiento
train_texts = []
for _, row in df.iterrows():
    text = f"Brand: {row['Brand']}\nModel: {row['Model']}\nYear: {row['model_year']}\nClass: {row['vehicle_class']}\nType: {row['vehicle_type']}\nCharge Time: {row['charge_time_minutes']} minutes\nBattery Life: {row['battery_life_km']} km\nRange: {row['range_km']} km\nEngine Size: {row['engine_size_L']} L\nCylinders: {row['engine_cylinder']}\nTransmission: {row['transmission_type']}\nEfficiency: {row['combined_wh_km']} Wh/km\nPrice: ${row['price_dollars']}\n\n"
    train_texts.append(text)

# Guardar los textos en un archivo
with open('train.txt', 'w') as f:
    for text in train_texts:
        f.write(text)

# Cargar el tokenizer y el modelo
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Preparar el dataset
dataset = TextDataset(
    tokenizer=tokenizer,
    file_path='train.txt',
    block_size=1024)

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=False)

# Configurar el entrenamiento
training_args = TrainingArguments(
    output_dir="./gpt2-cars",
    overwrite_output_dir=True,
    num_train_epochs=5,
    per_device_train_batch_size=8,
    save_steps=20,
    save_total_limit=2,
    learning_rate=2e-5
)

# Iniciar el entrenamiento
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset,
)

trainer.train()

import pickle

# Guardar el modelo y el tokenizer
with open('car_model.pkl', 'wb') as f:
    pickle.dump((model, tokenizer), f)


