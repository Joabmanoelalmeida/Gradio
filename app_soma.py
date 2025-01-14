import gradio as gr

def soma(num1, num2):
    return num1 + num2

print(soma(1, 2))

iface = gr.Interface(
    fn = soma,
    inputs = ["number", "number"], 
    outputs="number",
    title="Soma de dois números",
    description="Essa aplicação soma dois números",
    theme="default"   
)

iface.launch()
