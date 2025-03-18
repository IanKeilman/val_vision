from graphviz import Digraph

# Create a new directed graph
dot = Digraph(comment='YouTube Video Processing Pipeline', format='png')

# Define nodes for each pipeline stage
dot.node('A', 'Download Video\n(yt-dlp)')
dot.node('B', 'Extract Frames')
dot.node('C', 'Gameplay Classification\n(YOLO Classifier)')
dot.node('D', 'Decision:\nGameplay?')
dot.node('E', 'Crop Regions\n(Killfeed, Time, Minimap)')
dot.node('F', 'Object Detection\n(YOLO on Killfeed)')
dot.node('G', 'OCR on Detected Boxes')
dot.node('H', 'Discard Frame\n(Not Gameplay)', shape='box', style='filled', color='lightgrey')

# Connect the nodes with edges to represent the flow
dot.edge('A', 'B')
dot.edge('B', 'C')
dot.edge('C', 'D')
dot.edge('D', 'E', label='Yes')
dot.edge('D', 'H', label='No', style='dashed')
dot.edge('E', 'F', label='Killfeed Region')
dot.edge('F', 'G')

# Render the graph to a file (e.g., pipeline_graph.png) and display it
dot.render('pipeline_graph', view=True)

