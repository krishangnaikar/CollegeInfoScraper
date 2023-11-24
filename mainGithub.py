import csv

import html2text
import pandas as pd
import requests
from bs4 import BeautifulSoup

import funcs

urls = main.GetLinks()
df = pd.DataFrame()
page_links = []
for i in range(len(urls)):
    page_links.append(urls[i])
    href_links = funcs.GetPageLinks(urls[i])
    for x in range(len(href_links)):
        page_links.append(href_links[x])
college_links = []
for i in range(len(page_links)):
    college_links = funcs.GetColleges(page_links[i])
    for x in range(len(college_links)):
        df = funcs.GetCollegeInfo(college_links[x], df)

sheet = df.values.tolist()

"""
drive_scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',  # Include Drive scope for write access
    'https://www.googleapis.com/auth/drive.file'  # Another scope for write access
]

service_account_file = 'client_secret2s.json'

# Create credentials using the Service Account JSON file
credentials = Credentials.from_service_account_file(service_account_file, scopes=drive_scope)

# Create a Google Drive API service

file = gspread.authorize(credentials)
workbook = file.open("College info")
sheet = workbook.worksheet(title="Lined-Up-Info") # Change the title name here
other_sheet = workbook.worksheet(title="Majors")
"""
full_sheet = []
full_sheet.append(['', 'Links', 'Id',	'UNITID',	'College',	'Address',	'General Info',	'Website',	'Type',	'Awards',	'Campus Setting',	'Campus Housing',	'Student Population',	'Student to Teacher Ratio',	'Admissions Link',	'Application Link',	'Financial Aid',	'Net Price Calculator Link',	'Tuition Policies for Service members and Veterans',	'Disability Services',	'Athletic Graduation Rates',	'Majors',	'In State Tutions',	'Out of State Tutions',	'Books and Supplies',	'On Campus Room and board',	'On Campus Other',	'Off Campus Room and Board',	'Off Campus Other',	'# of Total Applicants',	'# of Male Applicants',	'# of Female Applicants',	'# of Accepted Applicants',	'# of Acceptated Males',	'# of Accepted Females'	'# of Enrolled Applicants',	'# Of Males Enrolled',	'# of Women Enrolled',	'Full Time Enrollments',	'Male Full Time Enrollments',	'Female Full Time Enrollemnts',	'Part Time',	'Male Part Time',	'Female Part Time',	'# Of Applicants Submmited SAT',	'% Of Applicants Subbmited With SAT',	'# Of Applicants Submmited ACT'	'% Of Applicants Subbmited With ACT',	'# of Applicants SAT Reading 25 percentile',	'# of Applicants SAT Reading 75 percentile',	'# of Applicants SAT Math 25 percentile',	'# of Applicants SAT Math 75 percentile',	'ACT Composite 25 percentile',	'ACT Composite 75 percentile',	'ACT English 25',	'ACT English 75',	'ACT Math 25',	'ACT Math 75',	'SAT / ACT',	'Other Test (Wonderlic,WISC-III,etc)',	'English Proficiency Test'])
for i in range(len(sheet)):
    i_before = i
    try:
        with open("Id.txt", 'r') as f:
            csv_reader = csv.reader(f)
            try:
                i = int(list(csv_reader)[0][-1])
                if (i == -1):
                    break
            except:
                i = i_before
    except FileNotFoundError:
        i = i_before


    if not(sheet[i] == None):
        # URL of the webpage you want to convert
        url = sheet[i][20]  # Replace with the desired URL
        url = "https://nces.ed.gov/collegenavigator/?id=" + url




        # Fetch HTML content from the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:

            def find_row(rows, target_content):
                found_row = None
                i = 0
                for row in rows:
                    if target_content == row:
                        found_row = i
                        return found_row
                    i+=1



            # Extract the HTML content
            html_content = response.text

            # Create an html2text instance
            html_parser = html2text.HTML2Text()

            # Convert HTML to plain text
            plain_text = html_parser.handle(html_content)

            # Print the plain text
            #print(plain_text)
            list_of_stuff = plain_text.split('![open-close](images/open.gif)')

            tuitions = []
            all_stuff = list_of_stuff[2].split("Total Expenses| 2019-2020| 2020-2021| 2021-2022| 2022-2023| % change 2021-2022")[-1].split('\n')
            list_of_stuff[2].split("Total Expenses| 2019-2020| 2020-2021| 2021-2022| 2022-2023| % change 2021-2022")[
                -1].split('\n')
            for b in range(len(all_stuff)):
                if (all_stuff[b] == "![close](images/close_tag.gif)"):
                    break
                else:
                    if ('|' in all_stuff[b]):
                        tuitions.append(all_stuff[b].split('|')[-2])
            #print(list_of_stuff)
            """
            for stuff in list_of_stuff:
                print(stuff.split('\n')[0])
            """

            list_without_pipes = []
            final_list = []

            #print(list_of_stuff[9])

            for line in list_of_stuff[9].split('\n'):
                if not('|' in line) and not('*' in line) and not('(' in line):
                    list_without_pipes.append(line)

            for line in list_without_pipes:
                if not(line == '' or line == '\n' or line == ' ' or line == '  ' or line == 'Completions are the number of awards conferred by program and award' or line == "Programs/Majors"):
                    final_list.append(line)

            ProgramsMajors = '\n'.join(final_list)
            row = sheet[i]
            try:
                next_row_id = sheet[i+1][21]
            except IndexError:
                next_row_id = -1

            #print(list_of_stuff[6])
            tests = []
            y = 0
            for z in range(len(list_of_stuff[6].split('\n'))):
                if (list_of_stuff[6].split('\n')[z] == "(Test Optional)| Not considered (Test Blind)  "):
                    y = z + 2
                    while (list_of_stuff[6].split('\n')[y] != '  '):
                        tests.append(list_of_stuff[6].split('\n')[y])
                        y += 1
            #print(tests)
            test_name = []
            results = []
            for test in tests:
                test_name.append(test.split('|')[0])
                results.append(test.split('|')[1:])
            # Required to be considered| Not required, but considered (Test Optional)| Not considered (Test Blind)
            #print(results)
            interpereted_results = {key: None for key in test_name}
            for result, test in zip(results, test_name):
                if (result[2] == " X  "):
                    interpereted_results[test] = ("Not considered (Test Blind)")
                elif (result[0] == " X"):
                    interpereted_results[test] = ("Required to be considered")
                elif (result[1] == " X"):
                    interpereted_results[test] = ("Not required, but considered (Test Optional)")


            links = []

            soup = BeautifulSoup(response.content, 'html.parser')

            # Tabs Content
            RightContent = soup.find('div', id='RightContent')
            divs = RightContent.find_all('div')
            detailOff = divs[21]
            tabconstraint = detailOff.find('div')
            if tabconstraint is not None:
                tableGen = tabconstraint.find('table')

                try:
                    addLink = tableGen.find('tr').find_all('td')[1].find('a').text
                except IndexError:
                    addLink = ''
                links.append(addLink)

                try:
                    appLink = tableGen.find_all('tr')[1].find_all('td')[1].find('a').text
                except IndexError:
                    appLink = ''
                links.append(appLink)

                try:
                    aidLink = tableGen.find_all('tr')[2].find_all('td')[1].find('a').text
                except IndexError:
                    aidLink = ''
                links.append(aidLink)

                try:
                    netLink = tableGen.find_all('tr')[3].find_all('td')[1].find('a').text
                except IndexError:
                    netLink = ''
                links.append(netLink)

                try:
                    policiesLink = tableGen.find_all('tr')[4].find_all('td')[1].find('a').text
                except IndexError:
                    policiesLink = ''
                links.append(policiesLink)

                try:
                    disabilityLink = tableGen.find_all('tr')[5].find_all('td')[1].find('a').text
                except IndexError:
                    disabilityLink = ''
                links.append(disabilityLink)

                try:
                    athleticGradRatesLink = tableGen.find_all('tr')[6].find_all('td')[1].find('a').text
                except IndexError:
                    athleticGradRatesLink = ''
                links.append(athleticGradRatesLink)
            try:
                if (len(tuitions) != 0):
                    if not (tuitions[0] == "Type of Plan"):
                        #row[12] = tuitions[-1]
                        if (len(tuitions) == 8):
                            row[13] = tuitions[1]
                            row[14] = tuitions[2]
                            row[15] = tuitions[3]
                            row[16] = tuitions[5]
                            row[17] = tuitions[6]
                            row[18] = tuitions[7]
                        elif (len(tuitions) == 1):
                            row[13] = tuitions[0]
                            row[14] = tuitions[0]
                            row[15] = tuitions[0]
                            row[16] = tuitions[0]
                            row[17] = tuitions[0]
                            row[18] = tuitions[0]
                        elif (len(tuitions) == 3):
                            row[13] = tuitions[0]
                            row[14] = tuitions[1]
                            row[15] = tuitions[2]
                            row[16] = tuitions[0]
                            row[17] = tuitions[1]
                            row[18] = tuitions[2]
                        else:
                            row[13] = "No Info"
                            row[14] = "No Info"
                            row[15] = "No Info"
                            row[16] = "No Info"
                            row[17] = "No Info"
                            row[18] = "No Info"
                else:
                    row[13] = "No Info"
                    row[14] = "No Info"
                    row[15] = "No Info"
                    row[16] = "No Info"
                    row[17] = "No Info"
                    row[18] = "No Info"
                """
                addLink = ''
        appLink = ''
        aidLink = ''
        netLink = ''
        policiesLink = ''
        disabilityLink = ''
        athleticGradRatesLink = ''
                """
                for j in range(len(links)):
                    row.append(links[j])
                row.append(interpereted_results[test_name[0]])
                row.append(interpereted_results[test_name[1]])
                row.append(interpereted_results[test_name[2]])
                row.append("")

            except IndexError:
                if (len(tuitions) != 0):
                    if not (tuitions[0] == "Type of Plan"):
                        # row[12] = tuitions[-1]
                        if (len(tuitions) == 8):
                            row[13] = tuitions[1]
                            row[14] = tuitions[2]
                            row[15] = tuitions[3]
                            row[16] = tuitions[5]
                            row[17] = tuitions[6]
                            row[18] = tuitions[7]
                        elif(len(tuitions) == 1):
                            row[13] = tuitions[0]
                            row[14] = tuitions[0]
                            row[15] = tuitions[0]
                            row[16] = tuitions[0]
                            row[17] = tuitions[0]
                            row[18] = tuitions[0]
                        elif (len(tuitions) == 3):
                            row[13] = tuitions[0]
                            row[14] = tuitions[1]
                            row[15] = tuitions[2]
                            row[16] = tuitions[0]
                            row[17] = tuitions[1]
                            row[18] = tuitions[2]
                    row.append("No Info")
                    row.append("No Info")
                    row.append("No Info")
                    row.append("")
                else:
                    row[13] = "No Info"
                    row[14] = "No Info"
                    row[15] = "No Info"
                    row[16] = "No Info"
                    row[17] = "No Info"
                    row[18] = "No Info"
                    row.append("No Info")
                    row.append("No Info")
                    row.append("No Info")
                    row.append("")

            for x in range(len(ProgramsMajors.split('\n'))):


                row[-1] = ProgramsMajors.split('\n')[x]
                full_sheet.append(row)

                with open('Majors.csv', 'a') as f:
                    # using csv.writer method from CSV package
                    write = csv.writer(f)
                    try:
                        write.writerow(row)
                    except UnicodeEncodeError:
                        write.writerow(["" for l in row])

                with open("Id.txt", 'w') as f:
                    write = csv.writer(f)
                    if not(next_row_id == -1):
                        write.writerow([i+1])
                    else:
                        write.writerow([-1])

            #v_cell = sheet.cell(i, 22)
            #v_cell.value = ProgramsMajors

            #sheet.update_cells([v_cell])


            print("Row:", i)



        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    else:
        exit(0)



# Function to remove blank rows from a CSV file
def remove_blank_rows(input_path, output_path):
    with open(input_path, "r", newline="") as infile, open(output_path, "w", newline="") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            # Check if all fields in the row are empty (blank)
            if not all(field == ""for field in row):
                # Write non-blank rows to the output CSV file
                write_bool = True

                for field in row:
                    if (field == "Programs/Majors"):
                        write_bool = False
                if (write_bool):
                    writer.writerow(row)

remove_blank_rows('Majors.csv', 'Majors2.csv')
