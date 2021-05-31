# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=None, types=[str, int, float], has_headers=False, delimiter=',',silence_error=True):
    '''
    Parse a CSV file into a list of records
    '''
    
    if select and not has_headers and not silence_error: 
        raise RuntimeError('select requires column headers')
    
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        records = []
        # Read the file headers
        if not has_headers:
            headers = next(rows)
        
            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select
            else:
                indices = []

        
            
            for row in rows:
                if not row:    # Skip rows with no data
                    continue

                if indices:
                    row = [ row[index] for index in indices ]

                if types:
                    try:
                        row = [func(val) for func, val in zip(types, row) ]                        
                    except ValueError as e:
                        if not silence_error:
                            print(f"Row {rowno}: Couldn't convert {row}")
                            print(f"Row {rowno}: Reason {e}")
                        continue


                record = dict(zip(headers, row))
                records.append(record)
                
        else:  
            records = list(map(tuple, rows))

    return records
