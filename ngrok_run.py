from pyngrok import ngrok, conf

conf.get_default().auth_token = "3BPQ6KlkUNdIVSNTPHxWOpsnOU7_45S6C3WCMEjCqbGqNfNea"

url = ngrok.connect(8000)
print("URL ngrok kamu:", url)

input("Tekan Enter untuk stop...")