import csv
import os
# =================
# CHANGE THESE 
# =================
TABLE_NAME = "dc_tree_final"
CSV_FILE = "tree_fix_v1.csv"
OUTPUT_FILE = "updates_v2.sql"

with open(CSV_FILE, "r", encoding="utf-8") as infile:
    sample = infile.read(1024)
    infile.seek(0)
    dialect = csv.Sniffer().sniff(sample)
    reader = csv.DictReader(infile, dialect=dialect)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:
        row_count = 0
        # Change the column names and your variables 
        for row in reader:
            common = row.get("common_name", "").strip()
            scientific = row.get("scientific_name", "").strip()

            # Change these to your variables 
            if not common or not scientific:
                continue

            # Change the esc_common and esc_scientific to esc_'Variable' and change the column names
            esc_common = common.replace("'", "''")
            esc_scientific = scientific.replace("'", "''")
            # Change table name and your column and variable names again 
            sql = (
                f"UPDATE {TABLE_NAME} "
                f"SET scientific_name = '{esc_scientific}' "
                f"WHERE common_name = '{esc_common}';\n"
            )

            outfile.write(sql)
            row_count += 1

print(f"Finished! Created {OUTPUT_FILE} with {row_count} updates.")
print("File location:", os.path.abspath(OUTPUT_FILE))
