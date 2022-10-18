import camelot
tables=camelot.read_pdf('foo.pdf',pages='1',flavor='lattice')
print(tables)
tables.export('foo.csv',f='csv', compress=False)