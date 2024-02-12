import openaikey
print("欢迎使用openaikey生成器,选项(1)生成key,(2)删除key,(3)查询key额度,(4)保存key,(5)查看所有key是否有效")
key=[]
while True:
    a=input("请输入你的选项:")
    if a=="1":
        a1=openaikey.add-key.add-key
        if a==None:
            print("没有这个key,请换一个key试试")
        else:
            key.append(a1)
    if a=="2":
        a2=input("请输入key")
        a1=openaikey.del-key.del-key(a2)
        if a1=="no":
            print("没有这个key")
        else:
            del key[key.index(a1)]
            print("删除成功")
    if a=="3":
        a2=input("请输入key")
        a1=openaikey.shart-key.shart-key(a2)
        print(a1)
    if a=="4":
        for i in range(len(key)):
            openaikey.seva-key.seva-key(key[i])
        print("保存成功")
    if a=="5":
        for i in range(len(key)):
            a3=openaikey.many-key.many-key(key[i]) 
            print(a3)
            
            
            
            
    
        
        
        
        
            
            

