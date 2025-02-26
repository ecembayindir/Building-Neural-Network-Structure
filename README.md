<h1 align="center">Neural Network Structure Using Neo4j Graph Database</h1>

<br/>

<h2>🚀 <strong>Objective</strong></h2>
<p>
This project aims to construct a neural network structure using the Neo4j graph database. The objective is to model a neural network using only Neo4j and Python, without relying on popular libraries like TensorFlow. The project includes development of stored procedures containing Cypher queries implemented in Java.
</p>

<h2>🔧 <strong>Technologies Used</strong></h2>
<div align="center">
    <img src="https://img.shields.io/badge/neo4j-4581C3?style=for-the-badge&logo=neo4j&logoColor=white" alt="Neo4j"/>
    <img src="https://img.shields.io/badge/java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white" alt="Java"/>
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python"/>
    <img src="https://img.shields.io/badge/maven-C71A36?style=for-the-badge&logo=apache-maven&logoColor=white" alt="Maven"/>
    <img src="https://img.shields.io/badge/IntelliJ_IDEA-000000?style=for-the-badge&logo=intellij-idea&logoColor=white" alt="IntelliJ IDEA"/>
</div>

<h2>📂 <strong>Project Summary</strong></h2>
<p>
The project demonstrates how to build and train a neural network directly within a graph database environment. By leveraging Neo4j's native graph structure, neural networks can be modeled in their most natural form - as interconnected nodes (neurons) with weighted relationships. This approach provides unique insights into neural network operations and demonstrates the potential of graph databases in machine learning applications.
</p>

<h2>📈 <strong>Methodology</strong></h2>
<ul>
  <li><strong>Graph-Based Neural Network:</strong> Models neurons as nodes and connections as relationships in Neo4j.</li>
  <li><strong>Java Stored Procedures:</strong> Implements essential neural network operations as Neo4j procedures.</li>
  <li><strong>Python Integration:</strong> Utilizes Python for controlling the training process and interaction with the database.</li>
</ul>

<h2>🔍 <strong>Implementation Details</strong></h2>

<h3>📋 Project Structure</h3>
<ul>
  <li>Developed neural network components directly in the Neo4j graph database.</li>
  <li>Created Java stored procedures for efficient graph operations.</li>
  <li>Implemented a Python interface for training and evaluation.</li>
</ul>

<h3>📌 Neural Network Architecture</h3>
<ul>
  <li>Input Layer: 108 neurons for feature representation.</li>
  <li>Hidden Layer: 10 neurons with tanh activation function.</li>
  <li>Output Layer: 3 neurons (for Home/Draw/Away classification) with softmax activation.</li>
  <li>Task Type: Classification for football match results.</li>
</ul>

<h3>📌 Java Stored Procedures</h3>
<ul>
  <li><strong>nn.createNeuron:</strong> Creates neuron nodes with specified properties.</li>
  <li><strong>nn.createRelationShipsNeuron:</strong> Establishes weighted connections between neurons.</li>
  <li>Enhanced security using parameterized queries instead of string concatenation.</li>
  <li>Improved error handling with detailed logging.</li>
</ul>

<h3>📌 Python Integration</h3>
<ul>
  <li>Modified Neo4jGraphAsNetwork.py to interact with Java stored procedures.</li>
  <li>Implemented batch processing for improved performance.</li>
  <li>Added min-max scaling in normalization functions.</li>
  <li>Optimized forward pass and loss calculation methods.</li>
</ul>

<h2>📊 <strong>Key Improvements</strong></h2>
<ul>
  <li><strong>Security:</strong> Replaced string concatenation with parameterized queries to prevent injection risks.</li>
  <li><strong>Performance:</strong> Implemented batch processing for more efficient training.</li>
  <li><strong>Architecture:</strong> Updated network structure from regression to classification with appropriate activation functions.</li>
  <li><strong>Optimization:</strong> Increased learning rate from 0.0005 to 0.001 and reduced batch size from 121 to 32.</li>
</ul>

<h2>🔍 <strong>Implementation Workflow</strong></h2>
<ol>
  <li>Updated Python code to use stored procedures instead of direct Cypher queries.</li>
  <li>Created Maven project with required Neo4j dependencies.</li>
  <li>Implemented Java stored procedures with optimized execution.</li>
  <li>Generated JAR file and added it to Neo4j plugins directory.</li>
  <li>Modified Neo4j configuration to allow custom procedures.</li>
  <li>Tested and verified the neural network structure and operations.</li>
</ol>

<h2>📢 <strong>Contact</strong></h2>
<ul>
  <li><a href="https://www.linkedin.com/in/ecembayindir/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white" alt="LinkedIn"/></a></li>
  <li><a href="mailto:ecmbyndr@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white" alt="Email"/></a></li>
</ul>

<p align="center">&copy; 2025 Ecem Bayındır. All rights reserved.</p>

<hr/>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=ecembayindir&repo=Building-Neural-Network-Structure&label=Repository%20views&color=0e75b6&style=flat" alt="Repository Views">
</p>

