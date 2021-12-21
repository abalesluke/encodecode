dds = {'a':'z','b':'y','c':'x','d':'w','e':'v','f':'u','g':'t','h':'s','i':'r','j':'q','k':'p','l':'o','m':'n','n':'m','o':'l','p':'k','q':'j','r':'i','s':'h','t':'g','u':'f','v':'e','w':'d','x':'c','y':'b','z':'a',' ':' ','1':'0','2':'9','3':'8','4':'7','5':'6','6':'5','7':'4','8':'3','9':'2','0':'1'}

def encode(ui):
	msg_all = ''
	for charz in ui:
		try:
			if charz == charz.upper():
				x = dds.get(charz.lower())
				msg_all+=x.upper()
			else:
				x = dds.get(charz)
				msg_all+=x
		except:
			msg_all+=charz
	return msg_all

while True:
	ui = input("\nEnter msg to Encode/Decode: ")
	print('Result: '+encode(ui))
