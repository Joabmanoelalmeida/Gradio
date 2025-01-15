import gradio as gr
import numpy as np
from PIL import Image
import io
import base64

def slide(titulo, texto, imagem, cor_fundo, cor_texto):
    estilo = (
        f"color: {cor_texto};"
        f"background-color: {cor_fundo};"
        "padding: 10px;"
        "text-align: center;"
        #"border-radius: 10px;"
        #"box-shadow: 5px 5px 5px #888888;"
    )
    #return f'<div style="{estilo}"><h1>{titulo}</h1><p>{texto}</p><img src="data:image/png;base64,{imagem}" width="200px"></div>'
    
    #Retornando a imagem para base64 se estiver presente
    imagem_html = ""
    if imagem is not None:
        buffered = io.BytesIO()
        Image.fromarray(imagem).save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        img_html = (f'<img src="data:image/png;base64,{img_str}" width="200px">')
    
    imagem_html = f"""
        <div style="{estilo}">
            <h1>{titulo}</h1>
            <p>{texto}</p>
            {img_html}
        </div>
    """
    return imagem_html

iface = gr.Interface(
    fn=slide,
    inputs=[
        gr.Textbox(label="Título", placeholder="Digite o título aqui"),
        gr.Textbox(label="Texto", placeholder="Digite o texto aqui"),
        gr.Image(type="numpy", label="Imagem"),
        gr.ColorPicker(label="Cor de fundo"),
        gr.ColorPicker(label="Cor do texto")
    ],
    
    outputs=gr.HTML(label="Slide"),
    title="Criando um slide",
    description="Crie um slide personalizado"
)

iface.launch()

     