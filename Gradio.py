import gradio as gr

def addition(a, b):
    return a + b

app = gr.Interface(
    fn=addition,
    inputs=["number", "number"],
    outputs="number",
    title="Addition of Two Numbers",
)

app.launch(share=True)