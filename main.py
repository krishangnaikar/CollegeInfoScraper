from bs4 import BeautifulSoup
import requests
import pandas as pd
import openpyxl
def GetPageLinks(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    PagingControls = soup.find('div', id='ctl00_cphCollegeNavBody_ucResultsMain_divPagingControls', style='text-align:right', class_='colorful')
    Links_Not_Href = PagingControls.find_all('a')
    href_links = []
    for i in range(len(Links_Not_Href)):
        href_links.append(Links_Not_Href[i]['href'])
        href_links[i] = "https://nces.ed.gov/collegenavigator/" + href_links[i]

    if (len(href_links) > 0):
        href_links[0] = 0
        href_links.remove(0)
    return (href_links)


#GetPageLinks("https://nces.ed.gov/collegenavigator/?s=AL&l=92+93+94")

def GetLinks():
    link = "https://nces.ed.gov/collegenavigator/?s=CA&l=92+93+94"
    links = []
    # 40, 41 are the characters to change
    States = [
        'AL',
        'AK',
        'AZ',
        'AR',
        'AS',
        'CA',
        'CO',
        'CT',
        'DE',
        'DC',
        'FL',
        'GA',
        'GU',
        'HI',
        'ID',
        'IL',
        'IN',
        'IA',
        'KS',
        'KY',
        'LA',
        'ME',
        'MD',
        'MA',
        'MI',
        'MN',
        'MS',
        'MO',
        'MT',
        'NE',
        'NV',
        'NH',
        'NJ',
        'NM',
        'NY',
        'NC',
        'ND',
        'CM',
        'OH',
        'OK',
        'OR',
        'PA',
        'PR',
        'RI',
        'SC',
        'SD',
        'TN',
        'TX',
        'UT',
        'VT',
        'VI',
        'WA',
        'WV',
        'WI',
        'WY',
    ]

    for i in range(len(States)):
        temp = link
        temp = list(temp)
        temp[40] = States[i][0]
        temp[41] = States[i][1]
        temp = ''.join(map(str, temp))
        links.append(str(temp))

    return links
def GetColleges(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    resultCon = soup.find_all('div', class_='resultCon')[1]
    table = resultCon.find('table', class_='resultsTable')
    resultsW = table.find_all('tr', class_="resultsW")
    resultsY = table.find_all('tr', class_="resultsY")
    links = []
    State = {}
    results = list(resultsW).copy()

    for i in range(len(resultsY)):
        results.insert(i + 1, resultsY[i])

    for i in range(len(results)):
        result = results[i]
        td_result = result.find_all('td')
        td_link = td_result[-1]
        link = td_link.find('a')['href']
        link = "https://nces.ed.gov/collegenavigator/" + str(link)
        link = link.replace('fv', 'id')
        links.append(link)

    data = {"Links": links}
    df = pd.DataFrame(data)

    AL = []
    AK = []
    AZ = []
    AR = []
    AS = []
    CA = []
    CO = []
    CT = []
    DE = []
    DC = []
    FL = []
    GA = []
    GU = []
    HI = []
    ID = []
    IL = []
    IN = []
    IA = []
    KS = []
    KY = []
    LA = []
    ME = []
    MD = []
    MA = []
    MI = []
    MN = []
    MS = []
    MO = []
    MT = []
    NE = []
    NV = []
    NH = []
    NJ = []
    NM = []
    NY = []
    NC = []
    ND = []
    CM = []
    OH = []
    OK = []
    OR = []
    PA = []
    PR = []
    RI = []
    SC = []
    SD = []
    TN = []
    TX = []
    UT = []
    VT = []
    VI = []
    WA = []
    WV = []
    WI = []
    WY = []

    for link in links:
        # Assuming you have already defined the lists for each abbreviation as shown in the previous response

        classification = link[40:42]  # Extract the 40th and 41st characters for classification

        if classification == 'AL':
            AL.append(link)
        elif classification == 'AK':
            AK.append(link)
        elif classification == 'AZ':
            AZ.append(link)
        elif classification == 'AR':
            AR.append(link)
        elif classification == 'AS':
            AS.append(link)
        elif classification == 'CA':
            CA.append(link)
        elif classification == 'CO':
            CO.append(link)
        elif classification == 'CT':
            CT.append(link)
        elif classification == 'DE':
            DE.append(link)
        elif classification == 'DC':
            DC.append(link)
        elif classification == 'FL':
            FL.append(link)
        elif classification == 'GA':
            GA.append(link)
        elif classification == 'GU':
            GU.append(link)
        elif classification == 'HI':
            HI.append(link)
        elif classification == 'ID':
            ID.append(link)
        elif classification == 'IL':
            IL.append(link)
        elif classification == 'IN':
            IN.append(link)
        elif classification == 'IA':
            IA.append(link)
        elif classification == 'KS':
            KS.append(link)
        elif classification == 'KY':
            KY.append(link)
        elif classification == 'LA':
            LA.append(link)
        elif classification == 'ME':
            ME.append(link)
        elif classification == 'MD':
            MD.append(link)
        elif classification == 'MA':
            MA.append(link)
        elif classification == 'MI':
            MI.append(link)
        elif classification == 'MN':
            MN.append(link)
        elif classification == 'MS':
            MS.append(link)
        elif classification == 'MO':
            MO.append(link)
        elif classification == 'MT':
            MT.append(link)
        elif classification == 'NE':
            NE.append(link)
        elif classification == 'NV':
            NV.append(link)
        elif classification == 'NH':
            NH.append(link)
        elif classification == 'NJ':
            NJ.append(link)
        elif classification == 'NM':
            NM.append(link)
        elif classification == 'NY':
            NY.append(link)
        elif classification == 'NC':
            NC.append(link)
        elif classification == 'ND':
            ND.append(link)
        elif classification == 'CM':
            CM.append(link)
        elif classification == 'OH':
            OH.append(link)
        elif classification == 'OK':
            OK.append(link)
        elif classification == 'OR':
            OR.append(link)
        elif classification == 'PA':
            PA.append(link)
        elif classification == 'PR':
            PR.append(link)
        elif classification == 'RI':
            RI.append(link)
        elif classification == 'SC':
            SC.append(link)
        elif classification == 'SD':
            SD.append(link)
        elif classification == 'TN':
            TN.append(link)
        elif classification == 'TX':
            TX.append(link)
        elif classification == 'UT':
            UT.append(link)
        elif classification == 'VT':
            VT.append(link)
        elif classification == 'VI':
            VI.append(link)
        elif classification == 'WA':
            WA.append(link)
        elif classification == 'WV':
            WV.append(link)
        elif classification == 'WI':
            WI.append(link)
        elif classification == 'WY':
            WY.append(link)

    state_lists = {
        'AL': AL,
        'AK': AK,
        'AZ': AZ,
        'AR': AR,
        'AS': AS,
        'CA': CA,
        'CO': CO,
        'CT': CT,
        'DE': DE,
        'DC': DC,
        'FL': FL,
        'GA': GA,
        'GU': GU,
        'HI': HI,
        'ID': ID,
        'IL': IL,
        'IN': IN,
        'IA': IA,
        'KS': KS,
        'KY': KY,
        'LA': LA,
        'ME': ME,
        'MD': MD,
        'MA': MA,
        'MI': MI,
        'MN': MN,
        'MS': MS,
        'MO': MO,
        'MT': MT,
        'NE': NE,
        'NV': NV,
        'NH': NH,
        'NJ': NJ,
        'NM': NM,
        'NY': NY,
        'NC': NC,
        'ND': ND,
        'CM': CM,
        'OH': OH,
        'OK': OK,
        'OR': OR,
        'PA': PA,
        'PR': PR,
        'RI': RI,
        'SC': SC,
        'SD': SD,
        'TN': TN,
        'TX': TX,
        'UT': UT,
        'VT': VT,
        'VI': VI,
        'WA': WA,
        'WV': WV,
        'WI': WI,
        'WY': WY
    }

    max_length = max(len(lst) for lst in state_lists.values())

    # Create a new dictionary where lists are extended or padded to match the maximum length
    extended_state_lists = {state: lst + [None] * (max_length - len(lst)) for state, lst in state_lists.items()}

    # Create the DataFrame
    df2 = pd.DataFrame(extended_state_lists)
    df.to_csv("links.csv", mode = 'a', index=False, header=False)
    df2.to_csv("States_Links.csv", mode = 'a', index = False, header=False)
    return links


def GetCollegeInfo(url):
    GenInfo = ''
    website = ''
    type = ''
    awards = []
    Campus_Setting = ''
    Campus_Housing = ''
    Student_Population = ''
    ratio = ''
    addLink = ''
    appLink = ''
    aidLink = ''
    netLink = ''
    policiesLink = ''
    disabilityLink = ''
    athleticGradRatesLink = ''

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    dashboard = soup.find('div', class_="dashboard")
    if dashboard is not None:
        div = dashboard.find('div', class_='collegedash')
        div2 = div.find_all('div')[4]
        # Find College name and Address
        span = div2.find_all('span')[0]

        college = span.find('span', class_='headerlg').text
        span_elements = span.descendants
        address = ""
        for child in span_elements:
            if child is not None:
                address = child.text
            else:
                address = None

        # Top Content

        table = div2.find('table', class_='layouttab')

        # Create a dictionary
        GenInfoDict = {}

        GenInfoDict['Links'] = url
        GenInfoDict['College'] = college
        GenInfoDict['Address'] = address

        # Populate the dictionary with the desired information
        try:
            GenInfoDict['General Info'] = table.find_all('tr')[0].find_all('td')[1].text
        except IndexError:
            GenInfoDict['General Info'] = ''

        try:
            website = table.find_all('tr')[1].find_all('td')[1].find('a').text
        except IndexError:
            website = ''
        GenInfoDict['Website'] = website

        try:
            type = table.find_all('tr')[2].find_all('td')[1].text
        except IndexError:
            type = ''
        GenInfoDict['Type'] = type

        awards_temp = table.find_all('tr')[3].find_all('td')[1]
        awards = []
        for child in awards_temp:
            try:
                if child is not None:
                    if child.text != '':
                        awards.append(child.text)
            except IndexError:
                pass
        GenInfoDict['Awards'] = [awards]

        try:
            Campus_Setting = table.find_all('tr')[4].find_all('td')[1].text
        except IndexError:
            Campus_Setting = ''
        GenInfoDict['Campus Setting'] = Campus_Setting

        try:
            Campus_Housing = table.find_all('tr')[5].find_all('td')[1].text
        except IndexError:
            Campus_Housing = ''
        GenInfoDict['Campus Housing'] = Campus_Housing

        try:
            Student_Population = table.find_all('tr')[6].find_all('td')[1].text
        except IndexError:
            Student_Population = ''
        GenInfoDict['Student Population'] = Student_Population

        try:
            ratio = table.find_all('tr')[7].find_all('td')[1].text
        except IndexError:
            ratio = ''
        GenInfoDict['Student to Teacher Ratio'] = ratio

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
            GenInfoDict['Admissions Link'] = addLink

            try:
                appLink = tableGen.find_all('tr')[1].find_all('td')[1].find('a').text
            except IndexError:
                appLink = ''
            GenInfoDict['Application Link'] = appLink

            try:
                aidLink = tableGen.find_all('tr')[2].find_all('td')[1].find('a').text
            except IndexError:
                aidLink = ''
            GenInfoDict['Financial Aid'] = aidLink

            try:
                netLink = tableGen.find_all('tr')[3].find_all('td')[1].find('a').text
            except IndexError:
                netLink = ''
            GenInfoDict['Net Price Calculator Link'] = netLink

            try:
                policiesLink = tableGen.find_all('tr')[4].find_all('td')[1].find('a').text
            except IndexError:
                policiesLink = ''
            GenInfoDict['Tuition Policies for Servicemembers and Veterans'] = policiesLink

            try:
                disabilityLink = tableGen.find_all('tr')[5].find_all('td')[1].find('a').text
            except IndexError:
                disabilityLink = ''
            GenInfoDict['Disability Services'] = disabilityLink

            try:
                athleticGradRatesLink = tableGen.find_all('tr')[6].find_all('td')[1].find('a').text
            except IndexError:
                athleticGradRatesLink = ''
            GenInfoDict['Athletic Graduation Rates'] = athleticGradRatesLink
        else:
            return list(GenInfoDict)


        return list(GenInfoDict)
    else:
        return ["",]

"""
print('Starting')

urls = GetLinks()
df = pd.DataFrame()
page_links = []
for i in range(len(urls)):
    page_links.append(urls[i])
    href_links = GetPageLinks(urls[i])
    for x in range(len(href_links)):
        page_links.append(href_links[x])
college_links = []
for i in range(len(page_links)):
    college_links = GetColleges(page_links[i])
    for x in range(len(college_links)):
        df = GetCollegeInfo(college_links[x], df)
        print(df)
df.to_csv('college-info-data-final.csv')
"""