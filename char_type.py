import chardet

def cod_detect(file_rute):
  with open(file_rute, 'rb') as file:
    result = chardet.detect(file.read())
    return result['encoding']

#Function use


file_rute = '/Users/jona/Desktop/C_digos_Postales_Nacionales.csv'
codification = cod_detect(file_rute)

print("codificacion detectada", codification)