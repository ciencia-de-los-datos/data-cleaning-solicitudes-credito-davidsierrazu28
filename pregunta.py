"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
def clean_data():

    import pandas as pd
    df_solicitudes_creditos = pd.read_csv('solicitudes_credito (1).csv', sep=';')

    #Eliminar columna Unnames
    df_solicitudes_creditos.drop(['Unnamed: 0'],axis=1,inplace=True)

    #Columna sexo
    df_solicitudes_creditos['sexo'] = df_solicitudes_creditos ['sexo'].str.lower().astype(str).str.strip()

    #Tipo Emprendimiento
    df_solicitudes_creditos ['tipo_de_emprendimiento'].replace({'-':' '},inplace=True, regex=True)
    df_solicitudes_creditos ['tipo_de_emprendimiento'].replace({'_':' '},inplace=True, regex=True)
    df_solicitudes_creditos['tipo_de_emprendimiento'] = df_solicitudes_creditos ['tipo_de_emprendimiento'].str.capitalize().str.strip()

    #Idea de Negocio
    df_solicitudes_creditos ['idea_negocio'].replace({'-':' '},inplace=True, regex=True)
    df_solicitudes_creditos ['idea_negocio'].replace({'_':' '},inplace=True, regex=True)
    df_solicitudes_creditos['idea_negocio']= df_solicitudes_creditos ['idea_negocio'].str.capitalize().str.strip()

    #Barrio
    df_solicitudes_creditos['barrio'] = df_solicitudes_creditos['barrio'].str.replace("_","-").str.replace("-"," ").str.lower()

    #Estrato
    df_solicitudes_creditos['estrato'] = df_solicitudes_creditos['estrato'].astype(str).str.capitalize()

    #Comuna
    df_solicitudes_creditos['comuna_ciudadano'] = df_solicitudes_creditos['comuna_ciudadano'].astype(str).str.capitalize()

    #Fecha
    df_solicitudes_creditos['fecha_de_beneficio'] = pd.to_datetime(df_solicitudes_creditos['fecha_de_beneficio'], dayfirst=True)

    #Reemplazar signo peso a monto de credito, quitar espacios, tomar parte entera, reemplazar comas y convertir en entero
    df_solicitudes_creditos['monto_del_credito'] = df_solicitudes_creditos['monto_del_credito'].str.replace('$','',regex=True)
    df_solicitudes_creditos['monto_del_credito'].replace({',':''}, inplace=True, regex=True)
    df_solicitudes_creditos['monto_del_credito'] = df_solicitudes_creditos['monto_del_credito'].str.split('.').str[0]
    df_solicitudes_creditos['monto_del_credito'] = df_solicitudes_creditos['monto_del_credito'].astype(int)

    #línea_credito
    df_solicitudes_creditos ['línea_credito'].replace({'-':' '},inplace=True, regex=True)
    df_solicitudes_creditos ['línea_credito'].replace({'_':' '},inplace=True, regex=True)
    df_solicitudes_creditos ['línea_credito'] = df_solicitudes_creditos ['línea_credito'].astype(str).str.capitalize().str.strip()

    df_solicitudes_creditos.dropna(inplace=True)
    df_solicitudes_creditos.drop_duplicates(inplace=True)

    return df_solicitudes_creditos

