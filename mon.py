import pyshark

cap = pyshark.FileCapture('/home/Userdir/Dokumente/networkmon/capture.cap', display_filter="dns")

def dns_cap():
    for pkt in cap:
        print(pkt.dns.qry_name)

dns_cap()
print('----------------------------------------------------------------------------------------------------')

def tcp_cap():
    for pkt in cap:
        print(pkt.dns.qry_name)

tcp_cap()
print('----------------------------------------------------------------------------------------------------')
