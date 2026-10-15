# Gradio creates a simple web interface for our agent.
import gradio as gr
import json
import os

# Import Agent 1 from our existing project.
from agents.email_triage_agent import analyze_email


def analyze_from_interface(email_text):
    """
    Receive email text from the web interface
    and send it to Agent 1.
    """

    # Prevent empty input from being sent to the model.
    if not email_text.strip():
        return "Please enter an email first."

    # Run our existing phishing triage agent.
    result = analyze_email(email_text)
   
    return json.dumps(result, indent=2)


# Create the web interface.
demo = gr.Interface(
    fn=analyze_from_interface,

    # Large text box where the user pastes an email.
    inputs=gr.Textbox(
        lines=12,
        label="Email",
        placeholder="Paste an email here..."
    ),

    # Display Agent 1's result.
    outputs=gr.Textbox(
        lines=12,
        label="Agent Analysis"
    ),

    title="PhishGuard AI",
    description="Agent 1 — Email Triage & Social Engineering Analysis",
)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))

    demo.launch(
        server_name="0.0.0.0",
        server_port=port
    )