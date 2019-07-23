import pyshark

# def dns_cap():
#     cap_dns = pyshark.FileCapture('/home/UserDir/Dokumente/networkmon/capture.cap', display_filter="dns")
#     for pkt in cap_dns:
#         print(pkt.dns.qry_name, pkt.ip.dst)
#
# dns_cap()
# print('----------------------------------------------------------------------------------------------------')

# def tcp_cap():
#     cap_tcp = pyshark.FileCapture('/home/UserDir/Dokumente/networkmon/capture.cap', display_filter="tcp")
#     for pkt in cap_tcp:
#         print('Communication IPs: ', pkt.ip.dst, ':', pkt.ip.src)
#         print('---------------------------------------------------------------------------------------------')
#         print('The following Ports are used: ', pkt.tcp.srcport, ':', pkt.tcp.dstport)
#
# ':', pkt.dns.qry_name   , ':', pkt.dns.resp_name
# tcp_cap()

#def protocol_cap():
 #   cap_protocol = pyshark.FileCapture('/home/UserDir/Dokumente/networkmon/capture.cap', display_filter="tcp")
 #   for pkt in cap_protocol:
  #      print('Communication IPs: ', pkt.ip.dst, ':', pkt.ip.src)
   #     print('---------------------------------------------------------------------------------------------')
    #    print('The following Ports are used: ', pkt.tcp.srcport, ':', pkt.tcp.dstport)


#protocol_cap()



cap_dns = pyshark.FileCapture('/home/UserDir/Dokumente/networkmon/capture.cap', display_filter="dns")
def dns_cap():

    if cap_dns.srcport == 80:
        for pkt in cap:
                print(pkt.dns.qry_name, ':', pkt.ip.src, 'from - to', pkt.ip.dst)
                print('---------------------------------------------------------------------------------------------')
                print( pkt.ip.src, 'from - to', pkt.ip.dst, ':', pkt[pkt.transport_layer].dstport, 'Port')

protocol_cap()

