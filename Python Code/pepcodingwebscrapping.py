import requests
from bs4 import BeautifulSoup as bsp
import webbrowser 
def printAllDeatils(urls):
    url=urls
    r=requests.get(url)
    htmlv=r.content
    soup=bsp(htmlv,"html.parser")
    value=soup.find("ol", class_="row collapsible classResource")
    allLi=value.find_all("li")
    dicMain={}

    for i in allLi:

        x=i.find("div",class_="collapsible-header bold")
        
        if x:
            print()
            print("                  ",x.text.strip().replace("\n","").replace("\r","").strip())
            print()
            
        y=i.find_all("div",class_="collapsible-body")
        dic={}
        count=1
        for j in y:

            listValue=j.find_all("li",class_="collection-item")

            for mainValue in listValue:
                print(count,end=" ")
                print("   ",mainValue.text.strip())
                
                ans=mainValue.text.strip().replace(' ','-')
                dic[count]=f"{url}/{ans}"
                count+=1

            print()
        if x:
            dicMain[x.text.strip().replace("\n","").replace("\r","").strip()]=dic
    print("\n\n")
    
    value=input("Enter Value =")
    value1=int(input(f"In {value} where you want to go :-"))
    print("\n\n")
    url=dicMain[value][value1]
    r=requests.get(url)
    htmlv=r.content
    soup=bsp(htmlv,"html.parser")
    value=soup.find("ul", class_="collection")
    value2=value.find_all("li")
    count=1
    dict1={}
    print("Question In",value1," are\n")
    for i in value2:
        print(count,end=" ")
        x=i.find("a").get("href")
        
        print("  ",i.find("span",class_="name").text.strip())
        dict1[count]=x
        count+=1
    print("\n\n\n")
    choice=int(input("Which Question You Want To Do \n"))
    url3="https://pepcoding.com"+dict1[choice]
    print(url3)
    webbrowser.open_new_tab(url3)

# This is Main Function 
url="https://pepcoding.com/resources/"
r=requests.get(url)
htmlv=r.content
soup=bsp(htmlv,"html.parser")
values=soup.find_all("div", class_="card free-resource-card show-on-hover border-radius")
count=1
dict={}
print("\n")
for value in values:

    print(count,end="  ")
    print(value.find("h2").text.strip()) 
    x=value.find("a").get("href")
    dict[count]=(f"https://pepcoding.com{x}")
    count+=1


print("\n\n\n")
choice=int(input("Enter Choice = "))

printAllDeatils(str(dict[choice]))