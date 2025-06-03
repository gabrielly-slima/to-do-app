from datetime import datetime

current_datetime = datetime.now()

def convert_to_portuguese ():
    # Converting days of the week from english to portuguese 
    acess_keys = list(week_pt.keys())

    for i in acess_keys:
        if i == week_day:
            value = week_pt[i]
            print(value)
            return value
    
    # converting months of the year from english to portuguese

def formating_date():
    formatted_date = (f"Hoje é {week_day}, dia {day} de {month} de {year}")
    return formatted_date

week_day = current_datetime.strftime("%A")
day = current_datetime.strftime("%d")
month = current_datetime.strftime("%B")
year = current_datetime.strftime("%Y")


week_pt = {"Sunday": "Domingo", "Monday":"Segunda-feira", 
          "Tuesday":"Terça-feira","Wednesday":"Quarta-feira",
          "Thursday":"Quinta-feira","Friday":"Sexta-feira","Saturday":"Sábado"}

months_pt = {"janeiro": 1,"fevereiro": 2,"março": 3,"abril": 4,
        "maio": 5,"junho": 6,"julho": 7,"agosto": 8,"setembro": 9,
        "outubro": 10,"novembro": 11,"dezembro": 12}

convert_week_to_pt()