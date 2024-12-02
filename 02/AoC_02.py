# Read Data
def read_data(filename):
    l_reports = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            line = line.split(" ")
            report = []
            for i in line:
                report.append(int(i))
            l_reports.append(report)
    return l_reports

def is_safe(report):
    if report[0] > report[1]:
        for i in range(len(report) - 1):
            diff = report[i] - report[i+1]
            if not (1 <= diff <= 3):
                return False
    else:
        for i in range(len(report) - 1):
            diff = report[i+1] - report[i]
            if not (1 <= diff <= 3):
                return False
    return True

def count_safe_reports(l_reports):
    num_safe_reports = 0
    for report in l_reports:
        if is_safe(report):
            num_safe_reports += 1
    return num_safe_reports

def is_safe_with_dampener(report):
    for ind in range(len(report)):
        test_report = report.copy()
        del test_report[ind]
        if is_safe(test_report):
            return True
    return False

def count_safe_report_with_dampener(l_reports):
    num_safe_reports = 0
    for report in l_reports:
        if is_safe_with_dampener(report):
            num_safe_reports += 1
    return num_safe_reports







# Main Program
l_reports = read_data("Input.txt")
print(count_safe_reports(l_reports))
print(count_safe_report_with_dampener(l_reports))

