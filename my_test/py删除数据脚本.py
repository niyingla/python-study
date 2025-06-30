import mysql.connector

# Establish database connection
conn = mysql.connector.connect(
    host='mysql-5632a4182a17-public.rds.volces.com',
    user='newlinktest',
    password='GRvDoXG#hh338x42',
    database='newlink10086'
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

# Loop through each table and execute the DELETE query in batches of 100,000
for (table,) in tables:
    while True:
        delete_query = f"""
            DELETE FROM {table}
            WHERE tenant_id != 103049
            LIMIT 100000
        """
        try:
            cursor.execute(delete_query)
            conn.commit()  # Commit the transaction
            print(f"Deleted rows from {table}")

            # Check if there are more rows to delete
            cursor.execute(f"SELECT COUNT(*) FROM {table} WHERE tenant_id != 103049")
            remaining_rows = cursor.fetchone()[0]
            if remaining_rows == 0:
                break
        except Exception as e:
            print(f"Error in {table}: {e}")
            break

# Close the cursor and connection
cursor.close()
conn.close()