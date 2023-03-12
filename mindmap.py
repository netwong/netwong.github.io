import streamlit as st
import openai
from pyvis.network import Network

# Set up OpenAI API credentials
openai.api_key = "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"

# Define a function to generate a mind map
def generate_mind_map(prompt):
    # Call the OpenAI API to generate a response
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    # Extract the response text from the API response
    response_text = response.choices[0].text.strip()

    # Process the response text to create a list of nodes and edges for the mind map
    nodes = []
    edges = []
    for line in response_text.split("\n"):
        if line.startswith("- "):
            nodes.append(line[2:])
        elif line.startswith("  - "):
            edges.append((nodes[-1], line[4:]))

    # Create a new network object
    network = Network()

    # Add the nodes to the network
    for node in nodes:
        network.add_node(node)

    # Add the edges to the network
    for edge in edges:
        network.add_edge(edge[0], edge[1])

    # Generate the network map
    network.show("mind_map.html")

# Set up the Streamlit app
st.title("ChatGPT Mind Map Generator")

# Create a text area for the user to input their prompt
prompt = st.text_area("Enter your ChatGPT prompt here:")

# Create a button to generate the mind map
if st.button("Generate Mind Map"):
    generate_mind_map(prompt)
    st.markdown("### Mind Map")
    st.components.v1.html(open("mind_map.html", "r").read(), width=800, height=600)
