import gradio as gr
from mylib.calculator import add


def calculate_sum(num1, num2):
    result = add(num1, num2)
    return result


with gr.Blocks() as demo:
    with gr.Row():
        number1 = gr.Number(label="First Number")
        number2 = gr.Number(label="Second Number")
    output = gr.Number(label="Sum")
    calc_btn = gr.Button("Calculate Sum")
    calc_btn.click(fn=calculate_sum, inputs=[number1, number2], outputs=output)

demo.launch()
