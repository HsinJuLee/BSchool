import os
import psycopg2
import csv

conn = psycopg2.connect(os.environ['DATABASE_URL'])
cur = conn.cursor()

reader = csv.reader(open('../../data/LondonYear_2013-2014.csv', 'rb'))
next(reader, None)

for row in reader:
    statement = \
        "INSERT INTO house_sales (price, date, post_code, property_type, whether_newbuild, freehold, address1, address2, address3, address4, town, local_authority, county, record_status, post_code_clean, inner_outer, borough_code, borough_name, ward_code14, ward_name14, ward_code13, ward_name13, msoall, lsoall, oall) VALUES (%(price)s, %(date)s, %(post_code)s, %(property_type)s, %(whether_newbuild)s, %(freehold)s, %(address1)s, %(address2)s, %(address3)s, %(address4)s, %(town)s, %(local_authority)s, %(county)s, %(record_status)s, %(post_code_clean)s, %(inner_outer)s, %(borough_code)s, %(borough_name)s, %(ward_code14)s, %(ward_name14)s, %(ward_code13)s, %(ward_name13)s, %(msoall)s, %(lsoall)s, %(oall)s)"

    commandParameters = {
        'price': row[1],
        'date': row[2],
        'post_code': row[7],
        'property_type': row[8],
        'whether_newbuild': row[9],
        'freehold': row[10],
        'address1': row[11],
        'address2': row[12],
        'address3': row[13],
        'address4': row[14],
        'town': row[15],
        'local_authority': row[16],
        'county': row[17],
        'record_status': row[18],
        'post_code_clean': row[19],
        'inner_outer': row[20],
        'borough_code': row[21],
        'borough_name': row[22],
        'ward_code14': row[23],
        'ward_name14': row[24],
        'ward_code13': row[25],
        'ward_name13': row[26],
        'msoall': row[27],
        'lsoall': row[28],
        'oall': row[29]
        }

    cur.execute(statement, commandParameters)
    # conn.commit()

cur.close()
conn.close()

# Table creation script
# CREATE TABLE house_sales
# (
#   id bigserial NOT NULL,
#   price numeric,
#   date date,
#   post_code character varying(10),
#   property_type character(1),
#   whether_newbuild character(1),
#   freehold character(1),
#   address1 character varying(100),
#   address2 character varying(100),
#   address3 character varying(100),
#   address4 character varying(100),
#   town character varying(100),
#   local_authority character varying(100),
#   county character varying(100),
#   record_status character(1),
#   post_code_clean character varying(100),
#   inner_outer character varying(10),
#   borough_code character varying(100),
#   ward_code14 character varying(100),
#   ward_name14 character varying(100),
#   ward_code13 character varying(100),
#   ward_name13 character varying(100),
#   msoall character varying(100),
#   lsoall character varying(100),
#   oall character varying(100),
#   borough_name character varying(100),
#   CONSTRAINT house_sales_pkey PRIMARY KEY (id)
# )
# WITH (
#   OIDS=FALSE
# );