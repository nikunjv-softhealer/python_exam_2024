# 8) Print the value of key ‘history’ from the below dict
sampleDict ={
    "class":{
        "student":{
            "name":"mike",
            "marks":{
                'physics': 70,
                'history': 80
            }
        }
    }
}

target_value = sampleDict['class']['student']['marks']['history']
print(target_value)