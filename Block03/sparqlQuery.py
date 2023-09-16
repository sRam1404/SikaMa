#!/usr/bin/python3
from rdflib import Graph, URIRef
from rdflib.namespace import RDFS, SKOS
import sys

def main():
    if len(sys.argv) > 1:
        queryFunc(sys.argv[1]) #Take user input via command line
    else:
        print("Please enter the right keyword for the query! Keywords are: PartHeirarchyNumber, EntriesWithMissingPartHeirarchyNumber, ProductDataSheet, EntriesWithMissingProductDataSheet")

def queryFunc(case):
    input = Graph()
    input.parse('Onto_Sika.ttl') #Import the database in ttl format

    if case == "PartHeirarchyNumber": #send the query to the database based on keywords
        queryOut = input.query('''
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX sika: <https://onto4all.com/en/ontologies/834/>
        SELECT ?Product ?PartHeirarchyNumber
            WHERE {
                ?Product sika:value_partheirarchynum ?PartHeirarchyNumber.
                FILTER NOT EXISTS {
                    ?Product sika:value_partheirarchynum ""^^xsd:string .
                    }
        }
        ''')
    elif case == "EntriesWithMissingPartHeirarchyNumber":
        queryOut = input.query('''
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
            '''
        )
    elif case == "ProductDataSheet":
        queryOut = input.query(''' 
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX sika: <https://onto4all.com/en/ontologies/834/>
        SELECT ?Product ?PartHeirarchyNumber ?FileName_ProductDataSheet
            WHERE {
                ?Product sika:value_productinformationsheet ?FileName_ProductDataSheet.
                ?Product sika:value_partheirarchynum ?PartHeirarchyNumber.
                FILTER NOT EXISTS {
                    ?Product sika:value_productinformationsheet ""^^xsd:string .
                    }
        }
        ''')
    elif case == "EntriesWithMissingProductDataSheet":
        queryOut = input.query('''
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX sika: <https://onto4all.com/en/ontologies/834/>
        SELECT ?Product ?PartHeirarchyNumber ?FileName_ProductDataSheet
            WHERE {
                ?Product sika:value_productinformationsheet ?FileName_ProductDataSheet.
                ?Product sika:value_partheirarchynum ?PartHeirarchyNumber.
                ?Product sika:value_productinformationsheet ""^^xsd:string.
        }
        '''
        )
    else: #If the keyword is unknown, print this
        print("Sorry! I cannot answer to you at this moment! I will connect you to our customer support.")

    #Print the query output
    for row in queryOut:
        for entry in row:
            if entry:
                print(entry)
            else:
                print("This entry is missing. Initiating ML assisted data crawling to fill in this information.")

main()
