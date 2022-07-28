from django.shortcuts import render

# Create your views here.
def data(request):  
    global data
    try:
        if request.method == "POST": 
            city=request.POST["location"]
            from requests_html import HTMLSession 
            session=HTMLSession()
            data=dict()
            url=f'https://www.google.com/search?q=weather+in+{city}' 
            out=session.get(url) 
            temp_c=out.html.find('span#wob_tm',first=1).text 
            data["temp_c"]=temp_c
            time=out.html.find('div#wob_dts',first=1).text 
            data["time"]=time 
            temp_f=out.html.find('span#wob_ttm',first=1).text 
            data["temp_f"]=temp_f 
            perci=out.html.find('span#wob_pp',first=1).text
            data["perci"]=perci 
            humidity=out.html.find('span#wob_hm',first=1).text 
            data["humidity"]=humidity
            wind=out.html.find('span#wob_tws',first=1).text 
            data["wind"]=wind
            climate=out.html.find('span#wob_dc',first=1).text 
            data["climate"]=climate 
            loc=out.html.find('div#wob_loc',first=1).text  
            data["loc"]=loc
        return render(request,"index.html",{'data':data}) 
    except: 
        return render(request,"index.html")

        
        