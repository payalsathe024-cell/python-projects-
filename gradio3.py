import gradio as gr
import ollama


# Function to generate AI response
def chatbot(message):

    response = ollama.chat(
        model="gemma:2b",
        messages=[
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return response["message"]["content"]


# Gradio Interface
demo = gr.Interface(
    fn=chatbot,
    inputs=gr.Textbox(
        label="Enter your question"),

    outputs=gr.Textbox(label="AI Response"),
    title="Simple Ollama Chatbot",
    description="Ask any question and get a response from Ollama."
)


# Launch
demo.launch(share=True)