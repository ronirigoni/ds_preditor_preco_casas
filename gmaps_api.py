'''
Esta função recebe um endereço ou um cep como parâmetro e realiza um request à API do Google.
Se bem sucedido, as coordenadas de Latitude e Longitude são retornadas. 
Caso não encontre o endereço ou ocorra algum outro problema, 'None' é rotornado.
'''
def busca_coordenadas(endereco_ou_cep):

    import googlemaps

    # Coloque sua google api key em um arquivo nomeado como: minha_google_api_key.txt
    GOOGLE_API_KEY = 'utilize_sua_propria_google_api_key'

    # O arquivo minha_google_api_key.txt é ignorado pelo Git
    with open('minha_google_api_key.txt') as f:
        GOOGLE_API_KEY = f.readline()

    gmaps = googlemaps.Client(key=GOOGLE_API_KEY)

    # Buscando o Geocoding do endereço
    gmaps_retorno = gmaps.geocode(endereco_ou_cep)

    # Se não encontrou o endereço ou ele está fora do perímetro de Palmas, retorna um erro:
    if len(gmaps_retorno) == 0:
        raise SystemExit("Endereço não encontrado! Confira e tente novamente.")

    lat = gmaps_retorno[0]['geometry']['location']['lat']
    lng = gmaps_retorno[0]['geometry']['location']['lng']

    # Se as coordenas do endereço estão fora do perímetro de Palmas, retorna erro também:
    if (int(lat) != -10) or (int(lng) != -48):
        raise SystemExit("Endereço fora do perímetro de Palmas! Confira e tente novamente.")

    return lat, lng