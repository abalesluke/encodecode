dds = {'a':'z','b':'y','c':'x','d':'w','e':'v','f':'u','g':'t','h':'s','i':'r','j':'q','k':'p','l':'o','m':'n','n':'m','o':'l','p':'k','q':'j','r':'i','s':'h','t':'g','u':'f','v':'e','w':'d','x':'c','y':'b','z':'a',' ':' '}

def encode(ui):
	msg_all = ''
	for charz in ui:
		try:
			x = dds.get(charz)
			msg_all+=x
		except:
			msg_all+=charz
	print(msg_all)

while True:
	ui = input("\n Enter msg to Encode/Decode: ")
	encode(ui)
