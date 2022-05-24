from django.shortcuts import render,HttpResponse
from Sparql_queries.queries import get_data


def index(request):
    sparqlQueries = get_data()
    
    data = {}

    # judges = sparqlQueries.case2_judge_name()
    # print(judges)
    # data = {
    #         "name":judges,
    #         'flag':True,
    #         'suffix':'judges',
    #         'title':'Judge of Case2'
            
    #        }
    
    if(request.method=='POST'):
        
        casename = request.POST['Case_name']
        question = request.POST['Question']
        #print(casename)
        #print(question)

        if(casename == 'K.T. Varghese & Ors VS. State of Kerala & Ors. on 24/01/2008' and question == 'List all court officials that come under the case.'):
            
            judges = sparqlQueries.case2_judge_name()
            #print(judges)
            data = {
                "name":judges,
                'flag':True,
                'suffix':'judges',
                'title':'Judge of Case2'
                
             }

            return render(request,'index.html', context = data)
     
        if(casename == 'K.T. Varghese & Ors VS. State of Kerala & Ors. on 24/01/2008' and question == 'List all the parties that come under the case?'):
            party = sparqlQueries.case2_party_name()
            
            data = {
                "name":party,
                'flag':True,
                'suffix':'judges',
                'title':'Judge of Case2'
                
           }   
        
        

            return render(request,'index.html', context = data)

        if(casename == 'K.T. Varghese & Ors VS. State of Kerala & Ors. on 24/01/2008' and question == 'Who is the Petitioner of the case?'):
            petitioner = sparqlQueries.case2_petitioner_name()
            
            data = {
                "name":petitioner,
                'flag':True,
                'suffix':'judges',
                'title':'Judge of Case2'
                
           }   
        
        

            return render(request,'index.html', context = data)    

        
        if(casename == 'K.T. Varghese & Ors VS. State of Kerala & Ors. on 24/01/2008' and question == 'What is the Case No. of the case?'):
            caseNumber = sparqlQueries.case2_case_number()
            
            data = {
                "name":caseNumber,
                'flag':True,
                'suffix':'judges',
                'title':'Judge of Case2'
                
           }   
        
        

            return render(request,'index.html', context = data)


        if(casename == 'Thakur Pratap Singh VS. Shri Krishna Gupta & Ors. on 02/12/1952' and question == 'What is the Case No. of the case?'):
            caseNumber = sparqlQueries.case1_case_number()
            
            data = {
                "name":caseNumber,
                'flag':True,
                'suffix':'judges',
                'title':'Judge of Case2'
                
           }   
        
        

            return render(request,'index.html', context = data) 


        if(casename == 'Thakur Pratap Singh VS. Shri Krishna Gupta & Ors. on 02/12/1952' and question == 'Who is the Petitioner of the case?'):
            petitioner = sparqlQueries.case1_petitioner_name()
            
            data = {
                "name":petitioner,
                'flag':True,
                'suffix':'judges',
                'title':'Judge of Case2'
                
           }   
        
        

            return render(request,'index.html', context = data) 

        if(casename == 'Thakur Pratap Singh VS. Shri Krishna Gupta & Ors. on 02/12/1952' and question == 'List all the parties that come under the case?'):
            party = sparqlQueries.case1_party_name()
            
            data = {
                "name":party,
                'flag':True,
                'suffix':'judges',
                'title':'Judge of Case2'
                
           }  

            return render(request,'index.html', context = data)


        if(casename == 'Thakur Pratap Singh VS. Shri Krishna Gupta & Ors. on 02/12/1952' and question == 'List all court officials that come under the case.'):
            judges = sparqlQueries.case1_judge_name()
            #print(judges)
            data = {
                "name":judges,
                'flag':True,
                'suffix':'judges',
                'title':'Judge of Case2'
                
           }   
        
        

            return render(request,'index.html', context = data)
        
        
    
    
         

    return render(request,'index.html')
    