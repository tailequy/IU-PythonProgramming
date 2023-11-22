# Update Data
# Running the code below will update the “active” column for the “David White” record
# from 0 (inactive) to 1 (active).
import sqlalchemy as db
def main():
    # get engine object using pymysql driver for mysql
    engine = db.create_engine("mysql+pymysql://root:168098205@localhost/movie")
    meta_data = db.MetaData()
    # get connection object
    connection = engine.connect()
    # get actor table definition
    actor_table = db.Table("actor", meta_data, autoload=True,
                           autoload_with=engine)
    # set update sql statement. update column 'active' to true
    #where id is equal to 3
    sql_query = db.update(actor_table).values(active=True).where(actor_table.columns.id==3)
    results = connection.execute(sql_query)
if __name__ == '__main__':
    main()