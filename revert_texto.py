import gradio as gr 

def texto_revertido(texto):
    texto_revertido = texto[::-1]
    return texto_revertido, len(texto_revertido)

iface = gr.Interface(
    fn=texto_revertido,
    inputs="text",
    outputs=["text", "number"],
    title="Texto revertido",
    description="Essa aplicação reverte um texto" 
)

iface.launch()

