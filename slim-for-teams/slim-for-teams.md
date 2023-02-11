# Slim full survey responses for Teams / Committees
This directory contains the relevant code to select only relevant columns / information for the different teams or committees, as per their responses.

## Creating the new .csv as requested
This reads in the validated csv files, and requires a python installation with the `pandas` package. I assume for this that the validated responses are located at `../..`, but this is something you can of course modify for your case if necessary.

Decide whether you want to compile the selection for staff, community1 with ID or community2 without ID (`'VS', 'VC1', 'VC2'`) and choose among `'WCT', 'WFC', 'WRC', 'WQAC', 'WDC', 'WST'`.

Check whether `scheme.py` contains the relevant column indices for the respective partial survey.

:information_source:  
Note / ToDo: `scheme.py` still needs the manually entered column indices for the community surveys, which do also contain some personal information. @WAC let's cross-check them together. For staff I believe I got all teams' indices already, but worth to check with our GoogleDoc ('Community Survey 2022 Question Compilation') if I missed something.

Once the relevant entries are there, get the selection like so:

```shell
python slim.py --group VS --team WFC
```

This prints out the original and the slimmed table (top and bottom few rows only for readability) so that you can cross-check what will be saved. The stored new csv will have the name `{survey_group}_{team_committee}_selected.csv'` and uses a comma `,` as separator, just like what we got as input.