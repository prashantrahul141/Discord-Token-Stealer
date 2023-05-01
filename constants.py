import os
BASE_DISCORD_URL = "https://discord.com/"
LOGIN_DISCORD_URL = BASE_DISCORD_URL + 'login'
QR_SVG_ELEMENT_SELECTOR = '#app-mount > div.appAsidePanelWrapper-ev4hlp > div.notAppAsidePanel-3yzkgB > div.app-3xd6d0 > div > div > div > div > form > div.centeringWrapper-dGnJPQ > div > div.transitionGroup-14WiKS.qrLogin-1ejtpI > div > div > div > div.qrCodeContainer-1qlybH > div.qrCodeOverlay-2bLtKl'
IMAGE_LOCATION = os.path.join(os.path.join(os.getcwd(), "screenshots"), "qr.png")
