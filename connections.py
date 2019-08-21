# -*- coding: utf-8 -*-

import azure.cosmos.cosmos_client as cc
import pandas as pd

def connect():
    config={'EndPoint':'https://ocrscan.documents.azure.com:443/',
                'PrimaryKey':'P81faodRwJMSjTRzPx4etkyYJrJVpAS0TEX5kaEN5AXAuyh73y8cAU2z1s3KyzfIRKaSwc7QE8FMgHFeaqnYqg==',
                'Database':'CognitiveAPIDemoDataSource',
                'Container':'PocCollection'}    
    client=cc.CosmosClient(url_connection=config['EndPoint'],
                           auth={'masterKey':config['PrimaryKey']})
    
    query={'query':'select * from c'}
    
    database_link='dbs/'+'CognitiveAPIDemoDataSource'
    container_link=database_link+'/colls/PocCollection'
    options = {}
    options['enableCrossPartitionQuery'] = True
    options['maxItemCount'] = 2
    items=client.QueryItems(container_link,query,options)
    lst=[]
    for item in iter(items):
        lst.append(item['text']['textDetails'])
        
    df=pd.DataFrame(lst,columns=['Feedback'])
    return df