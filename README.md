I needed a script to create multiple SQL update statements based off a .csv file. For the intended purpose I had one column as my “key” and it updated every sub column based on that key. For example, I had multiple unique common names tied to the same scientific name, so my key was the common name, since doing it in reverse would have overwritten the unique varieties. But this could be used to create any update statements when a join or window function wouldn’t work. 

I used a “DISTINCT” statement to create a table to export of each unique value, I added that to the same folder as the Python script. 

TABLE_NAME = The name of your table in SQL
CSV_FILE = The title of your csv 
OUTPUT_FILE = What you want your output to be called 

“Column 1” = The title from SQL for your first column
“Column 2” = The title from SQL for your second column 

Instructions are notes inside the code! Have fun and happy Querying 
