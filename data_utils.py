from datetime import datetime

current_datetime = datetime.now()

def convert_date_to_pt ():
    week_pt = {"Sunday": "domingo", 
               "Monday":"segunda-feira", 
                "Tuesday":"terça-feira",
                "Wednesday":"quarta-feira",
                "Thursday":"quinta-feira",
                "Friday":"sexta-feira",
                "Saturday":"sábado"}

    months_pt = {"January":"janeiro", "February":"fevereiro",
                "March":"maio", "April":"abril", "May":"maio",
                "June":"junho", "July":"julho","August":"agosto",
                "September":"setembro","October":"outubro",
                "November":"novembro","December":"dezembro"} 

    week_day = current_datetime.strftime("%A")
    day = current_datetime.strftime("%d")
    month = current_datetime.strftime("%B")
    year = current_datetime.strftime("%Y")  

    # Converting days of the week from english to portuguese 
    acess_keys_week = list(week_pt.keys())
    for i in acess_keys_week:
        if i == week_day:
            week_day = week_pt[i]
    
    acess_keys_month = list(months_pt.keys())
    for i in acess_keys_month:
        if i == month:
            month = months_pt[i]
    
    formatted_date = (f"Hoje é {week_day},\n dia {day} de {month} de {year}")
    return formatted_date
