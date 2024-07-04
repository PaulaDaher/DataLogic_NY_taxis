import streamlit as st
import pickle
import re
import requests
import io

# Configuración de la página de Streamlit
st.set_page_config(page_title="Chat", page_icon="💬", layout="wide")

@st.cache_resource
# Funcion para cargar el modelo
def load_model():
    # Ruta del modelo
    bucket_name = "modelosllm"
    object_name = "car_model.pkl"
    url = f"https://storage.googleapis.com/{bucket_name}/{object_name}"
    
    response = requests.get(url)

    # Crear un objeto de tipo archivo en memoria
    file_object = pickle.loads(response.content)
    
    return file_object

# Cargar el modelo
model, tokenizer = load_model()

# Función de generación de respuesta
def generate_response(prompt, model, tokenizer):
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    output = model.generate(input_ids, max_length=200, num_return_sequences=1, no_repeat_ngram_size=2)
    return tokenizer.decode(output[0], skip_special_tokens=True)

# Función para extraer información específica
def extract_info(text):
    info = {}
    patterns = {
        'Brand': r'Brand:\s*(\w+)',
        'Model': r'Model:\s*([\w\s]+)',
        'Year': r'Year:\s*(\d+)',
        'Class': r'Class:\s*(\w+)',
        'Type': r'Type:\s*(\w+)',
        'Charge Time': r'Charge Time:\s*(\d+)',
        'Battery Life': r'Battery Life:\s*(\d+)',
        'Range': r'Range:\s*(\d+)',
        'Engine Size': r'Engine Size:\s*([\d.]+)',
        'Cylinders': r'Cylinders:\s*(\d+)',
        'Transmission': r'Transmission:\s*(\w+)',
        'Efficiency': r'Efficiency:\s*([\d.]+)',
        'Price': r'Price:\s*\$(\d+)'
    }
    
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            info[key] = match.group(1)
    
    return info

# Función para elaborar la respuesta
def elaborate_response(info):
    responses = []
    
    if 'Brand' in info and 'Model' in info:
        responses.append(f"The {info['Brand']} {info['Model']} is a cutting-edge electric vehicle that exemplifies modern automotive engineering.")
    
    if 'Class' in info:
        responses.append(f"As a {info['Class'].lower()}, it offers a perfect balance of comfort and performance for discerning drivers.")
    
    if 'Range' in info:
        responses.append(f"With an impressive range of {info['Range']} km on a single charge, this vehicle is designed for long-distance travel without compromise.")
    
    if 'Charge Time' in info:
        responses.append(f"The advanced charging system allows for a full charge in just {info['Charge Time']} minutes, minimizing downtime and maximizing your mobility.")
    
    if 'Battery Life' in info:
        responses.append(f"The high-capacity battery is engineered to last up to {info['Battery Life']} km, ensuring long-term reliability and reducing environmental impact.")
    
    if 'Efficiency' in info:
        responses.append(f"With an energy efficiency of {info['Efficiency']} Wh/km, this vehicle sets a new standard in electric powertrain optimization.")
    
    if 'Price' in info:
        responses.append(f"Priced at ${info['Price']}, it represents a compelling value proposition in the electric vehicle market.")
    
    return ' '.join(responses)

# Función para la respuesta detallada
def generate_detailed_response(prompt, model, tokenizer):
    initial_response = generate_response(prompt, model, tokenizer)
    info = extract_info(initial_response)
    detailed_response = elaborate_response(info)
    return detailed_response

# Interfaz de Streamlit
st.title("Generador de información sobre autos eléctricos")

st.write("Este es un chat para generar información sobre las características de los autos recomendados")

prompt = st.text_input("Ingresa la marca y el nombre del auto:")

if st.button("Generar Información"):
    if prompt:
        response = generate_detailed_response(prompt, model, tokenizer)
        st.write(response)
    else:
        st.write("Por favor ingresa una marca y nombre de auto.")