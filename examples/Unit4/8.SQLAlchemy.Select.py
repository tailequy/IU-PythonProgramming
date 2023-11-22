#Select Data
#To select all records in the “actor” table, run the code shown below.
import sqlalchemy as db
def main():
    # get engine object using pymysql driver for mysql
    engine = db.create_engine("mysql+pymysql://root:168098205@localhost:3306/movie")
    meta_data = db.MetaData()
    # get connection object
    connection = engine.connect()
    # get actor table definition
    actor_table = db.Table("actor", meta_data, autoload=True, autoload_with=engine)
    # set the select statement
    select_actor = db.select([actor_table])
    # execute the select statement
    dataset = connection.execute(select_actor).fetchall()
    # print row by row
    for row in dataset:
        print(row)
if __name__ == '__main__':
    main()
