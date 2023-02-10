import numpy as np
import csv
import pandas as pd

survey_group = 'VS' # 'Staff'
#survey_group = 'VC1' # 'Community-1_withID'
#survey_group = 'VC2' # 'Community-2_noID'

main_path = 'WCA_Survey_2022/'

def survey_loader(fpath):
    # loads the survey as specified via the file path into a dataframe
    response = pd.read_csv(fpath)
    print(response)
    return response

def get_question_answer_scheme(dataframe):
    return dataframe[:1]

validated = survey_loader(f'{main_path}{survey_group}.csv')

only_true_responses = validated.iloc[1:]
question_answer_scheme = get_question_answer_scheme(validated)

def group_columns(q_and_a_scheme):
    main_groups = question_answer_scheme.keys().values
    specific_groups = question_answer_scheme.iloc[0].values
    return main_groups, specific_groups

general_q = np.arange(0,9)

main_groups, specific_groups = group_columns(question_answer_scheme)

def get_q_indices(main_g):
    q_start_stop = []
    for k in range(len(main_g)):
        if 'Unnamed' not in main_g[k]:
            starts = k
            for j in range(k,len(main_g)-1):
                if 'Unnamed' not in main_g[j+1]:
                    ends = j
                    break
            if k <= j:
                q_start_stop.append([k,j])
    return q_start_stop

q_start_stop = get_q_indices(main_groups)

def get_options(list_of_qs):
    multi_q = []
    single_q = []
    for i,el in enumerate(list_of_qs):
        if el[0] != el[1]:
            multi_q.append(i)
        else:
            single_q.append(i)
    return multi_q, single_q

def view_one_q(df, all_q, q):
    return df.iloc[:,all_q[q][0]:all_q[q][1]+1]

qs_with_multi_options, qs_with_single_option = get_options(q_start_stop)

true_qs_with_single_option = qs_with_single_option[9:]

