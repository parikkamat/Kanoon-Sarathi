from SPARQLWrapper import SPARQLWrapper, JSON , CSV
import pandas as pd
import numpy as np

class get_data:

    def __init__(self):
        self.sparql = SPARQLWrapper('https://kanoon.herokuapp.com/LegalCase/sparql')

    def case2_judge_name(self):
        
        self.sparql.setQuery("""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
        PREFIX dc: <http://purl.org/dc/elements/1.1/> 
        PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
        PREFIX schema: <http://schema.org/> 
        PREFIX : <http://example.org/#> 

        SELECT ?JudgesofCase2

        WHERE {
        ?Case dc:hasInstance :case2.
        :case2  dc:hasCourtOfficial ?Judges .
        ?Judges  rdfs:hasName ?JudgesofCase2 .
        }

        """
        )
        
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        
        judge = []
        for result in results["results"]["bindings"]:
              judge.append( result["JudgesofCase2"]["value"])
             
    
        return judge
    
    def case2_party_name(self):
        
        self.sparql.setQuery("""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
        PREFIX dc: <http://purl.org/dc/elements/1.1/> 
        PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
        PREFIX schema: <http://schema.org/> 
        PREFIX : <http://example.org/#> 

        SELECT ?PartiesOfCase2
        WHERE {
               ?Case dc:hasInstance :case2 .
               :case2 dc:hasParty ?Party .
               ?Party rdfs:hasName ?PartiesOfCase2 .
  
               }


        """
        )
        
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
       
        party = []
        for result in results["results"]["bindings"]:
              party.append( result["PartiesOfCase2"]["value"])
             
    
        return party 


    def case2_petitioner_name(self):
        
        self.sparql.setQuery("""

        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
        PREFIX dc: <http://purl.org/dc/elements/1.1/> 
        PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
        PREFIX schema: <http://schema.org/> 
        PREFIX : <http://example.org/#>
        SELECT ?PetitionerofCase2
        WHERE {
        ?Case dc:hasInstance :case2 .
        :case2 dc:hasParty :case2P1 .
        :case2P1 rdfs:hasName ?PetitionerofCase2 .
        }

        """
        )
        
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
       
        petitioner = []
        for result in results["results"]["bindings"]:
              petitioner.append( result["PetitionerofCase2"]["value"])
             
    
        return petitioner

    
    def case2_case_number(self):
        
        self.sparql.setQuery("""

        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
        PREFIX dc: <http://purl.org/dc/elements/1.1/> 
        PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
        PREFIX schema: <http://schema.org/> 
        PREFIX : <http://example.org/#>

        SELECT ?CaseNumberofCase2
        WHERE {
               ?Case dc:hasInstance :case2 .
               :case2 rdfs:hasCaseNo ?CaseNumberofCase2 .
              }


        """
        )
        
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
       
        caseNumber = []
        for result in results["results"]["bindings"]:
              caseNumber.append( result["CaseNumberofCase2"]["value"])
             
    
        return caseNumber


    def case1_case_number(self):
        
        self.sparql.setQuery("""

        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
        PREFIX dc: <http://purl.org/dc/elements/1.1/> 
        PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
        PREFIX schema: <http://schema.org/> 
        PREFIX : <http://example.org/#>

        SELECT ?CaseNumberofCase1
        WHERE {
               ?Case dc:hasInstance :case1 .
               :case1 rdfs:hasCaseNo ?CaseNumberofCase1 .
              }


        """
        )
        
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
       
        caseNumber = []
        for result in results["results"]["bindings"]:
              caseNumber.append( result["CaseNumberofCase1"]["value"])
             
    
        return caseNumber

    def case1_petitioner_name(self):
        
        self.sparql.setQuery("""

        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
        PREFIX dc: <http://purl.org/dc/elements/1.1/> 
        PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
        PREFIX schema: <http://schema.org/> 
        PREFIX : <http://example.org/#>

        SELECT ?PetitionerofCase1
        WHERE {
        ?Case dc:hasInstance :case1 .
        :case1 dc:hasParty :case1P1 .
        :case1P1 rdfs:hasName ?PetitionerofCase1 .
        }

        """
        )
        
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
       
        petitioner = []
        for result in results["results"]["bindings"]:
              petitioner.append( result["PetitionerofCase1"]["value"])
             
    
        return petitioner


    def case1_judge_name(self):
        
        self.sparql.setQuery("""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
        PREFIX dc: <http://purl.org/dc/elements/1.1/> 
        PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
        PREFIX schema: <http://schema.org/> 
        PREFIX : <http://example.org/#> 

        SELECT ?JudgesofCase1

        WHERE {
        ?Case dc:hasInstance :case1.
        :case1  dc:hasCourtOfficial ?Judges .
        ?Judges  rdfs:hasName ?JudgesofCase1 .
        }

        """
        )
        
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
       
        judge = []
        for result in results["results"]["bindings"]:
              judge.append( result["JudgesofCase1"]["value"])
             
    
        return judge        
    
    def case1_party_name(self):
        
        self.sparql.setQuery("""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
        PREFIX dc: <http://purl.org/dc/elements/1.1/> 
        PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
        PREFIX schema: <http://schema.org/> 
        PREFIX : <http://example.org/#> 

        SELECT ?PartiesOfCase1
        WHERE {
               ?Case dc:hasInstance :case1 .
               :case1 dc:hasParty ?Party .
               ?Party rdfs:hasName ?PartiesOfCase1 .
  
               }


        """
        )
        
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
       
        party = []
        for result in results["results"]["bindings"]:
              party.append( result["PartiesOfCase1"]["value"])
             
    
        return party

       