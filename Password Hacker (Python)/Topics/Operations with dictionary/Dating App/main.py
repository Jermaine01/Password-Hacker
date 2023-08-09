def select_dates(potential_dates):
    names = []
    for i in range(len(potential_dates)):
        if potential_dates[i]["age"] > 30 and potential_dates[i]["hobbies"].__contains__("art") \
                and potential_dates[i]["city"] == "Berlin":
            names.append(potential_dates[i]["name"])
    return str(', '.join(names))


