import gradio as gr

def customizar_texto(texto, cor_fundo, cor_texto, tamanho_fonte, estilo_fonte):
    estilo =(
        f"color: {cor_texto};"
        f"background-color: {cor_fundo};"
        f"font-size: {tamanho_fonte}px;"
        f"font-family: {estilo_fonte};"
    )
    return f'<div style="{estilo}">{texto}</div>'

iface = gr.Interface(
    fn=customizar_texto,
    inputs=[
        gr.Textbox(label="Texto", placeholder="Digite o texto aqui"),
        gr.ColorPicker(label="Cor de fundo"),
        gr.ColorPicker(label="Cor do texto"),
        gr.Slider(minimum=10, maximum=100, label="Tamanho da fonte", value=20),
        gr.Radio(choices=["Arial", "Times New Roman", "Courier New"], label="Estilo da fonte")
    ],

    outputs=gr.HTML(label="Texto customizado"),
    title="Customizando texto",
    description="Personalize o seu texto"
    
)

iface.launch()

    