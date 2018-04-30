There are two methods in this package:

expandEAV(eavdf)
Pass a pandas DataFrame in entity attribute value format
receive a pandas DataFrame in a schema table format

the column headers will be the unique set of attributes in the eav
the row indices will be the unique set of entities (records) in the eav

compressToEAV(schemadf)
pass a pandas DataFrame with 1 to many columns and at least one row
receive a pandas DataFrame in EAV format

IT IS NECESSARY TO SET NULL OR EMPTY ELEMENTS TO np.NaN
the returned DataFrame will have n records for each n datapoint
the first column will be filled with row indices
the second column will be filled with column headers
the third column will be filled with values
