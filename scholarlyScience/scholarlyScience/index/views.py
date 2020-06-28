from django.shortcuts import render
from .models import companies


def apphome(request):
    content=companies.objects.all()
    list1=[]
    list2=[]
    list3=[]
    for i in content:
        list1.append(i.location)
        list2.append(i.scale)
        list3.append(i.skill1)
        list3.append(i.skill2)
        list3.append(i.skill3)
        list3.append(i.skill4)
        list3.append(i.skill5)

    list_set=set(list1)
    list_scale=set(list2)
    list_tech=set(list3)
    
    scale=request.GET.get( 'scale')
    location=request.GET.get('location')
    tech=request.GET.get('tech')
    flag=[]
    flag1=[]
    for i in content:
        if tech==None:
            break
        elif tech==i.skill1:
            flag.append("skill1")
            flag1.append("skill1")
            # break
        elif tech==i.skill2:
            flag.append("skill2")
            flag1.append("skill2")
            # break
        elif tech==i.skill3:
            flag.append("skill3")
            flag1.append("skill3")
            # break
        elif tech==i.skill4:
            flag.append("skill4")
            flag1.append("skill4")
            # break
        elif tech==i.skill5:
            flag.append("skill5")
            flag1.append("skill5")
            # break
    flag=set(flag)
    flag1=set(flag1)
    flag=list(flag)
    flag1=list(flag1)
    
    # print(flag, flag1, '@@@@@@@@@@@@@@@@@@@')
    # j=''
    # for i in range(len(flag)):
    #     j=j+flag[i]+"="+flag1[i]+" , "
    
    # print(j, '@@@@@@@@@@@@@@@@@@@')
    if scale != None:
        content=companies.objects.filter( scale=scale)
    elif location !=None:
        content=companies.objects.filter( location=location)
    elif tech !=None:
        print('ssssssssssssssss')
        content=companies.objects.filter(skill4="AWS",  skill5="AWS")
        print('ssssssssssssssss')
    else:
        ''
    # c=c.split(',')
    # content=content.order_by(c)

    return render(request, 'index/home.html', {'content':content, 'list_set':list_set,'list_scale':list_scale, 'list_tech':list_tech })

#companies.object.filter()