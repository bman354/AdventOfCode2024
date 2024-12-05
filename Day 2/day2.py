with open('input.txt', 'r') as file:
    raw = file.readlines()

reports = [[int(x) for x in line.strip().split()] for line in raw]

def isSafe(report):
    #report is only safe when change in value from left to right is 1-3, and is consistantly increasing or decreasing 
    is_increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    is_decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))

    if not (is_increasing or is_decreasing):
        return False

    for i in range(len(report) - 1):
            if(report[i] == report[i+1]):
                return False
            if not(1 <= abs(report[i] - report[i+1]) <= 3):
                return False
            
    return True


def failSafe(report):
    if isSafe(report):
        return True
    
    for i in range(len(report)):
        temp_report = report[:i] + report[i + 1:]
        if isSafe(temp_report):
            return True

    return False

safe_count = sum(failSafe(report) for report in reports)


print("Number of safe reports: ", safe_count)