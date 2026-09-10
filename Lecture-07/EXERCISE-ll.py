def remove_duplicates(lst):
    return list(set(lst))

performance_data = {
    "Sales": {
        "Alice": [80,85,88,90],
        "Bob": [70,75,78,80],
        "Charlie": [60,65,70,72]
    },
    "Engineering": {
        "David": [90,92,94,95],
        "Eve": [85,88,87,90],
        "Frank": [88,87,86,85]
    },
    "HR": {
        "Grace": [70,72,74,76],
        "Heidi": [65,68,70,73],
        "Ivan": [60,62,64,66]
    }
}

# ข้อ 1
average_scores = {}
for depertment, employees in performance_data.items():
    average_scores[depertment] = {}
    for employee, scores in employees.items():
        averge = sum(scores) / len(scores)
        average_scores[depertment][employee] = averge
print("Average Performance Scores:",average_scores)


# ข้อ 2 
top_performer = {}
for depertment, employees in average_scores.items():
    top_performer[depertment] = {}
    score = 0
    for employee, scores in employees.items():
        if scores > score :
            score = scores
            top_performer[depertment][employee] = score    
print("Top Performers:",top_performer)    


# ข้อ 3 
best_department = {}
averge_depertment = {}
number = 0
for depertment, employees in average_scores.items():
    best_department[depertment] = {}
    list_scores = []
    for employee, scores in employees.items():
        list_scores.append(scores)
        averge = sum(list_scores) / len(list_scores)
    averge_depertment[depertment] = averge
    
for depertment, averge in averge_depertment.items():
    if averge > number:
        number = averge
        best_department.clear()
        best_department[depertment] = number
for key,value in best_department.items():
    print("Best Department:",key,value)
    

# ข้อ 4    
progress_scores = {}
for depertment, employees in performance_data.items():
    progress_scores[depertment] = {}
    for employee, scores in employees.items():
        list_scores_progress = []
        for i in range(len(scores)):
            for j in range(i+1,len(scores)):
                s = scores[i] - scores[j]
                list_scores_progress.append(s)
                progress_scores[depertment][employee] = list_scores_progress
                
depreciate_scores = []
for depertment, employees in progress_scores.items():
    for employee, scores in employees.items():
        for score in scores:
            if score > 0:
                depreciate_scores.append(employee)                
depreciate_scores = remove_duplicates(depreciate_scores)

develop_employee = {}
for depertment,employees in average_scores.items():
    develop_employee[depertment] = {}
    list_employee = []
    for employee, scores in employees.items():
        list_employee.append(employee)
        develop_employee[depertment] = list_employee

for depertment,employees in develop_employee.items():
    for employee in employees:
        for depreciate_employee in depreciate_scores:
            if depreciate_employee in employees:
                employees.remove(depreciate_employee)
print("Continuous Improers:",develop_employee)


#ข้อ 5 
print("Summary Report:")
for depertment, employees in average_scores.items():
    print("Department:",depertment)
    for employee, scores in employees.items():
        print("\t",employee,': Average Score =',scores)
    for depertment2, employees in top_performer.items() :
        if depertment == depertment2:
            for employee, scores in employees.items():
                print('Top Performer:',employee ,'with Averge Score = ',scores)

for key,value in best_department.items():
    print(f"\nBest Department: {key} with Average Score = {value:.2f}")