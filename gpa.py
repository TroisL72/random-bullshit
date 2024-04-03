import pandas as pd

def calculate_gpa(csv_file):
    
    df = pd.read_csv(csv_file)
    df = df.dropna(subset=['Final Results'])

    total_credit_hours = df['ECTS'].sum()
    total_quality_points = (df['ECTS'] * df['Final Results']).sum()

    if total_credit_hours != 0:
        gpa = total_quality_points / total_credit_hours
        return gpa
    else:
        return "Error"


csv_file_path = 'GPA - Sheet1.csv'
gpa = calculate_gpa(csv_file_path)
print("GPA:", gpa)
