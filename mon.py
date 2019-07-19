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




def protocol_cap():
    cap_protocol = pyshark.FileCapture('/home/UserDir/Dokumente/networkmon/capture.cap', display_filter="tcp")
    cap_dns = pyshark.FileCapture('/home/UserDir/Dokumente/networkmon/capture.cap', display_filter="dns")

    if cap_dns.srcport == 80:
        for pkt in cap_protocol and cap_dns:
                print('Communication IPs: ', pkt.ip.dst, ':', pkt.ip.src)
                print('---------------------------------------------------------------------------------------------')
    elif dns.src.port == 443:
        for pkt in cap_protocol and cap_dns:   
                print('Communication IPs: ', pkt.ip.dst, ':', pkt.ip.src)
                print('---------------------------------------------------------------------------------------------')
    else:
        for pkt in cap_protocol and cap_dns:
                print('The following Ports are used: ', pkt.tcp.srcport, ':', pkt.tcp.dstport)   

protocol_cap()

