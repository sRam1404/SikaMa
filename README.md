# SikaMa - Accurate and trustworthy information for Sika
A SIKA wide knowledge hub to overcome information barriers, with accurate and trustworthy information.

## Why is SikaMa necessary?
Imagine actively taking steps to reduce information gaps, without having to hunt for every last inefficiency out there in your knowledge management. What if you could overcome organizational silos, one regular CI/CD build at a time?
So, instead of firefighting when inefficiencies and information gaps arise, you stay ahead of the digital transformation curve with SikaMa.

## How does SikaMa work?
1) Knowledge Representation and Reasoning forms the backbone of this knowledge base (KB). 
2) The various stakeholders define what gaps are unacceptable. The construction industry, which is still in the nascent stages of digitalization could be missing critical information, like the product heirarchy numbers of SIKA products. The formulation of the gaps are used as key performance indicators (KPI), which can be objectively measured and quantified.
3) The test engineer can then convert these gap formulations into queries to test and verify the KB.
4) The missing entities, their properties are then provided to the ML-assisted data-crawler to find the necessary information from documents, web-pages and other sources (eventually norms, or other non-Sika documents as well).

# Working with the tool
There are four key components to realize SikiMa in its current iteration, and these components are depicted in the block diagram and described in detail in the following subsections:  

## Block diagram
![Block diagram of SikaMa](BlockDiagram.jpg)

## Block 1 - Unacceptable knowledge gaps as Key-performance indicator
Different stakeholders involved at Sika, like top-level management, product managers, engineers and sales persons, just to name a few personas, elicit what in their eyes would be an unacceptable gap to have in their information management.

As an example: *As a marketing and sales representative, it is important that every Sika product in the market should have a unique identifier, called as "Product Hierarchy Number."*

## Block 2 - Conversion of unacceptable knowledge gaps into SPARQL Queries using natural language like domain specific languages
Armed with the information on what gaps in knowledge should be actively bridged, test engineers could use natural language like domain specific languages to generate the SPARQL queries to interact with the knowledge base. 

```
Feature: sparql queries are generated to interact with the knowledge model to find the inconsistencies

  Scenario: find products missing product heirarchy number
     Given we have a list of the unacceptable information gaps, as defined by the stakeholders
      When we have an initial knowledge model
      Then select only those products which are missing product heirarchy number
```
Domain specific languages are used to reduce the complexity that is involved in writing these test cases. The generated SPARQL query would be:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX sika: <https://onto4all.com/en/ontologies/834/>
SELECT ?Product ?PartHeirarchyNumber
	WHERE {
		?Product sika:value_partheirarchynum ?PartHeirarchyNumber.
		?Product sika:value_partheirarchynum ""^^xsd:string  
}
```
## Block 3 - Interaction of the SPARQL queries with the knowledge base to identify inconsistencies in KB
(Insert screenshots)

## Block 4 - ML-assisted 

## Usage using Jupyter
- Download [Anaconda](https://www.anaconda.com/)
- Then open this repo with **Jupyter**, then you will be able to interact with this AI Assistent.

## Dependencies to run sparqlQuery.py
- Install rdblib - "pip install rdblib". More information on rdblib can be found [here](https://rdflib.readthedocs.io/en/stable/apidocs/rdflib.html#rdflib.graph.Graph.query).
- It is suggested to run the code in virtual environment.

# Current limitations

# Future challenges and further research

# Sources
