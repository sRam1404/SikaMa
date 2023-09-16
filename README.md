# SikaMa - Accurate and trustworthy information for Sika
A SIKA wide knowledge hub to overcome information barriers, with accurate and trustworthy information.

## Why is SikaMa necessary?
Imagine actively taking steps to reduce information gaps, without having to hunt for every last inefficiency out there in your knowledge management. What if you could overcome organizational silos, one regular CI/CD build at a time?
So, instead of firefighting when inefficiencies and information gaps arise, you stay ahead of the digital transformation curve with SikaMa.

## How does SikaMa work?
1) Knowledge Representation and Reasoning forms the backbone of this knowledge base (KB). 
2) The various stakeholders define what gaps are unacceptable. For example, the construction industry, which is still in the nascent stages of digitalization, could be missing critical information, like the product heirarchy numbers of Sika products. The formulation of the gaps are used as key performance indicators (KPI), which can be objectively measured and quantified.
3) The test engineer can then convert these gap formulations into queries to test and verify the KB.
4) The missing entities, their properties are then provided to the ML-assisted data-crawler to find the necessary information from documents, web-pages and other sources (eventually norms, or other non-Sika documents as well). The entities, its properties and values are then added to the KB.
5) A report of the improvement in the KPI achieved is provided as an objective measure to all the involved stakeholders.

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
More sample SPARQL queries are included [here](/Ontology/Query_Cases.txt).
## Block 3 - Interaction of the SPARQL queries with the knowledge base to identify inconsistencies in KB
An initial version of the domain ontology meta-model was created by manually selecting the relevant domain features and a first instance of the ontology with three product instances from the Sika range of products were chosen as a deliberate strategy to be sparse and quick in ontology creation. The ontology is uploaded [along with this repository](Ontology/Onto_Sika.ttl) and shown here. ![visualized here](/Ontology/Export_Ontology.JPG.jpg).

The query generated interacts with the sparsely populated KB and when found to be deficient, this information can be used by the ML-assisted data-crawler to find the relavant information to augment and grow the knowledge base continuously. The attached screenshot from Protege Desktop, an OWL editor tool is seen below, wherein the entities were deliberately left empty to start the data crawling with ML, which would then identify more items that might be missing one or the other property and value. ![Protege screenshot](/Ontology/Screenshot_Protege.png)

### Instructions to test out Protege as a tool, the sparse-KB and the query interaction
1. Install Protege Desktop Version 5.5.0-win (tested on Windows laptop).
2. Navigate to the folder where it was installed and click on ```run.bat``` to start Protege Desktop.
3. Download the [Onto_Sika.ttl](Ontology/Onto_Sika.ttl), click on ```File -> Open ->``` on Protege menu and navigate to the folder to which the file was downloaded to open the file.
4. Click on ```Run -> Start Reasoner``` and select ```HermiT``` as the reasoner.
5. Click on SPARQL Query tab and copy one of the SPARQL query from [here](/Ontology/Query_Cases.txt) and execute the query to get the results.

## Block 4 - ML-assisted data-crawler and named-entity disambiguation to augment the knowledge base and report the changes to the KPI
We fine tuned LLM App using LangChain, OpenAI, Python. Using Vector database like pinecone which follows steps of **embedding**, **indexing** and **querying**.
### Usage using Jupyter
- Download [Anaconda](https://www.anaconda.com/)
- Then open this repo with **Jupyter**, then you will be able to interact with this AI Assistent.

### Dependencies to run sparqlQuery.py
- Install rdblib - "pip install rdblib". More information on rdblib can be found [here](https://rdflib.readthedocs.io/en/stable/apidocs/rdflib.html#rdflib.graph.Graph.query).
- It is suggested to run the code in virtual environment.

# Future challenges and further research
- Extend the KPI's to find more unacceptable gaps by interacting with the stakeholders.
- Currently seen for internal purposes, purely to bridge gaps.
  - But SikaMa can be used to answer customer queries in the future.
  - A customer should only get back information that is freely available in the public-domain. Private, company-internal and confidential information should not be disclosed.
    
# Sources
