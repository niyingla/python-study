import time

import mysql.connector

# Establish database connection
conn = mysql.connector.connect(
    host='mysql-f0db9778c442-public.rds.volces.com',
    user='root',
    password='Qiyu@0630',
    database='newlink106703'
)
cursor = conn.cursor()

# Get all tables containing 'tenant_id' column
cursor.execute("""
    SELECT table_name
    FROM information_schema.columns
    WHERE table_schema = DATABASE() AND column_name = 'tenant_id'
""")

# Fetch all table names
tables = cursor.fetchall()

# Loop through each table
for (table,) in tables:
    while True:
        # Select ids to delete where tenant_id != 106703 (batch of 10,000)
        cursor.execute(f"""
            SELECT id FROM {table}
            WHERE tenant_id != 106703
            LIMIT 10000
        """)
        ids_to_delete = cursor.fetchall()

        # If no rows to delete, break out of the loop
        if not ids_to_delete:
            break

        # Prepare DELETE query for batch deletion
        ids = [str(row[0]) for row in ids_to_delete]
        ids_str = ",".join(ids)

        # Delete the selected rows in batches of 100,000
        delete_query = f"""
            DELETE FROM {table}
            WHERE id IN ({ids_str})
        """
        try:
            cursor.execute(delete_query)
            conn.commit()  # Commit the transaction
            print(f"Deleted {len(ids_to_delete)} rows from {table}")

            #睡眠0.5s
            time.sleep(0.5)

        except Exception as e:
            print(f"Error in {table}: {e}")
            break

# Close the cursor and connection
cursor.close()
conn.close()