#import numpy as np
import pandas as pd
import argparse
import scheme

parser = argparse.ArgumentParser(description="Setup survey groups and team")
parser.add_argument("--group", choices=['VS', 'VC1', 'VC2'], help="Group of respondents")
parser.add_argument("--team", choices=['WCT', 'WFC', 'WRC', 'WQAC', 'WDC', 'WST'], help="WCA Team or Committee")
args = parser.parse_args()

survey_group = args.group

team_committee = args.team

#survey_group = 'VS' # 'Staff'
#survey_group = 'VC1' # 'Community-1_withID'
#survey_group = 'VC2' # 'Community-2_noID'

def survey_loader(fpath):
    # loads the survey as specified via the file path into a dataframe
    response = pd.read_csv(fpath)
    print(response)
    return response

validated = survey_loader(f'../../{survey_group}.csv')

only_true_responses = validated.iloc[1:]

if survey_group == 'VS':
    columns = scheme.staff
elif survey_group == 'VC1':
    columns = scheme.community1
elif survey_group == 'VC2':
    columns = scheme.community2
    
print(columns)

interesting_columns = columns[team_committee]

selected = only_true_responses.iloc[:,interesting_columns]
print(selected)

selected.to_csv(f'{survey_group}_{team_committee}_selected.csv', sep=',', encoding='utf-8')