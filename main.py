def getDayInfo(data):
    months = {1 : "Января", 2: "Февраля", 3: "Марта", 4: "Апреля", 5: "Май", 6: "Июня", 
    7: "Июля", 8: "Августа", 9: "Сентября", 10: "Октября", 11: "Ноября", 12: "Декабря"}
    days = {1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг", 5: "Пятница", 6:"Суббота", 0: "Воскресенье"}
    data = list(map(int, data.split(".")))
    day, month, year = data
    
    a = (14 - month) // 12
    y = year - a
    m = month + 12 * a - 2
    day_of_week = (7000 + (day + y + y // 4 - y // 100 + y // 400 + (31 * m) // 12)) % 7

    print(f"{days[day_of_week]}, {day // 7 + 1} неделя {months[month]} {year} года")