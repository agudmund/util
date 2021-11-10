import requests as r

rez = r.get("https://accounts.spotify.com/authorize")

print(rez.status_code)
print(rez.text)

# https://open.spotify.com/track/5po7LnT5uPfQ7ftd25XZIh?si=N85z-DHtQwq4Z12H3ly-fw
# spotify:track:
# spotify:track:02XFGaXmsE8laElTx2kVNm

# BQBStdrmP8izPyQCX3amNzbt8KzvxRAMo_kNRT4k_QxeNoKHMpItUIwDTzBcI5UQLWc8Q83ruPqQ8u5lWdboDPOh32Gjx_GJZoe0pUJSxH5iE2BJsBytq9QsvcCrH7TgFcxQbU1lcZs5DxfQBHf4dYOwauk

# print (dir(rez))
# print(rez.__dict__)