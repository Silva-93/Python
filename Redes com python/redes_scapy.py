from scapy.config import conf
from scapy.layers.l2 import ARP, Ether
from scapy.layers.inet import IP, ICMP, UDP, traceroute
from scapy.layers.dns import DNS, DNSQR
from scapy.layers.dhcp import BOOTP, DHCP
from scapy.sendrecv import sr1, srp1, sendp
from scapy.sendrecv import sniff
from sys import exit



############### enviando um pacote de camada 2 ###############
MY_IP = '192.168.1.158'
MY_MAC = '3C-7C-3F-7B-D4-F5'
BROADCAST = 'ff:ff:ff:ff:ff'
MY_SERVER = '192.168.1.1'

pacote_ethernet = Ether(dst=BROADCAST)
pacote_arp = ARP(pdst=MY_SERVER)
pacote_final = pacote_ethernet / pacote_arp

respota = srp1(pacote_final, timeout=2)
# respota.show()


############### ICMP ###############

pacote = Ether()
pacote /= IP(dst='192.168.1.1')  # Tbm funciona com DNS
pacote /= ICMP()

result = srp1(pacote)
# result.show()


############### DNS ###############

def host_ip(url='ddg.gg'):
    packet = IP(dst=MY_SERVER)
    packet /= UDP(dport=53)
    packet /= DNS(qd=DNSQR(qname=url))

    return sr1(packet)

# host_ip()


############### traceroute ###############

resp, _ = traceroute('ddg.gg', verbose=False)
# resp.show()


############### DHCP ###############
pac = Ether(src=conf.iface.mac)
pac /= IP(src='0.0.0.0', dst='255.255.255.255')
pac /= UDP(sport=68, dport=67)
pac /= BOOTP(chaddr=MY_MAC)
pac /= DHCP(
    options=[
        ('message-type', 'discover'),
        'end'
    ]
)
# sendp(pac)


############### sniff ###############
def xpto(s):
    return s.summary()

try:
    sniff(filter='tcp', prn=xpto)

except KeyboardInterrupt:
    exit(0)

