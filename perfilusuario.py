import gradio as gr
from datetime import datetime

def selecionador(texto, idade, imagem,  lista_texto, cor, formacao):
    mensagem_boas_vindas = f"Bem-vindo(a), {texto}!"  
    ano_atual = datetime.now().year
    ano_nascimento = ano_atual - idade
    mensagem_imagem = "Sua foto de perfil recebida" if imagem else "Nenhuma imagem recebida"
    lista_processada = [[itens] for itens in lista_texto.splitlines()] if lista_texto else "Nenhum texto recebida"
    
    return(
        mensagem_boas_vindas,
        ano_nascimento,
        mensagem_imagem,
        lista_processada,
        f"Cor selecionada: {cor}",
        formacao
    )

iface = gr.Interface(
    fn=selecionador,
    inputs=[
        gr.Textbox(label="Nome", placeholder="Digite o seu nome completo aqui"),
        gr.Slider(minimum=0, maximum=100, label="Idade",  value=0),
        gr.Image(type="pil", label="Sua foto de perfil"),
        gr.Textbox(label="Descrição", lines=5, placeholder="Fale mais sobre você"),
        gr.ColorPicker(label="Selecione sua Cor favorita"),
        gr.CheckboxGroup(label="Formação", choices=["Engenheiro civil", "Engenheiro ambiental e sanitário", "Engenheiro quinmico"])
    ],
    
    outputs=[
        gr.Textbox(label="Mensagem de boas-vindas"),
        gr.Number(label="Ano de nascimento"),
        gr.Textbox(label="Imagem"),
        gr.DataFrame(label="Lista de texto", headers=["Itens"]),
        gr.Textbox(label="Cor selecionada"),
        gr.Textbox(label="Formação selecionada")
    ],
    title="Perfil do usuário",
    description="Descrição do perfil do usuário"
)

iface.launch()
