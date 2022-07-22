# Example Python program to serialize a pandas DataFrame

# into a PostgreSQL table

from sqlalchemy import create_engine

import psycopg2

import pandas as pds

 

 

# Data - Marks scored

studentScores = [(57, 61, 76, 56, 67),

                 (77, 67, 65, 78, 62),

                 (65, 71, 56, 63, 70)

                ];

# Create a DataFrame

dataFrame   = pds.DataFrame(studentScores,

              index=(1211,1212,1213), # Student ids as index

              columns=("Physics", "Chemistry", "Biology", "Mathematics", "Language")

              );

         

alchemyEngine           = create_engine('postgresql+psycopg2://postgres:admin123@localhost/test', pool_recycle=3600);

postgreSQLConnection    = alchemyEngine.connect();

postgreSQLTable         = "StudentScores";

 

try:

    frame           = dataFrame.to_sql(postgreSQLTable, postgreSQLConnection, if_exists='fail');

except ValueError as vx:

    print(vx)

except Exception as ex:  

    print(ex)

else:

    print("PostgreSQL Table %s has been created successfully."%postgreSQLTable);

finally:

    postgreSQLConnection.close();