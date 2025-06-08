#!/bin/python3.11
import sys
import time
import pywifi
from pywifi import const

print("python version %s"% sys.version)

'''
    1.iface status:
        iface.status()
        const.IFACE_DISCONNECTED 4
        const.IFACE_SCANNING     1
        const.IFACE_INACTIVE     2
        const.IFACE_CONNECTING   3
        const.IFACE_CONNECTED    0
    2.author algrithm
        profile
        const.AUTH_OPEN
        const.AUTH_SHARED
    3.key manage type
        const.AKM_TYPE_NONE
        const.AKM_TYPE_WPA
        const.AKM_TYPE_WPAPSK
        const.AKM_TYPE_WPA2
        const.AKM_TYPE_WPA2PSK
    4.password type
        const.CIPHER_TYPE_NONE
        const.CIPHER_TYPE_WEP
        const.CIPHER_TYPE_TKIP
        const.CIPHER_TYPE_CCMP
'''
class WiFi:
    def __init__(self):
        self.wifi = pywifi.PyWiFi()
        self.iface = self.wifi.interfaces()[0]  # get the first wireless controller
        self.results = []
        self.types = {}
        const_attrs = dir(const)
        constants = [attr for attr in const_attrs if attr.isupper()]
        self.types['IFACE_STATUS'] = {getattr(const, k): k for k in constants if 'IFACE' in k}
        self.types['AKM_TYPE'] = {getattr(const, k): k for k in constants if 'AKM_TYPE' in k}
        self.types['AUTH_ALG'] = {getattr(const, k): k for k in constants if 'AUTH_ALG' in k}
        self.types['CIPHER_TYPE'] = {getattr(const, k): k for k in constants if 'CIPHER_TYPE' in k}
        self.types['KEY_TYPE'] = {getattr(const, k): k for k in constants if 'KEY_TYPE' in k}
        print("wifi init done, iface 0 status %d!"% self.iface.status())

    def scan_wifi(self):
        print("scaning wifi...")
        self.iface.scan()                       # start scan
        time.sleep(2)                           # ensure scan done
        results = self.iface.scan_results()     # get scaned wifi list
        self.results = sorted(results, key=lambda x: x.signal, reverse=True)
        count = 0
        for result in self.results:
            ssid = result.ssid
            signal = result.signal
            freq = result.freq/1024/1024
            bssid = result.bssid
            if signal < -80:
                self.results.remove(result)
            else:
                print("\t[%2d] SSID: %-24s signal: %s dBm    freq: %.2f GHz    bssid: %s"%
                      (count, ssid, signal, freq, bssid))
            count += 1

    def show_profile(self, profile, index=0):
        print("\n[%2d] ssid: %s"% (index, profile.ssid))
        print("\tauth  : %s"% self.types['AUTH_ALG'][profile.auth])
        print("\takm   :", end='')
        for i, akm in enumerate(profile.akm):
            print("%s%s"% (' ' if not i else '\t'+' '*8, self.types['AKM_TYPE'][akm]))
        print("\tcipher: %s"% self.types['CIPHER_TYPE'][profile.cipher])
        print("\tkey   : %s"% profile.key)

    def show_connected_profiles(self):
        self.old_profiles = self.iface.network_profiles()
        for i, p in enumerate(self.old_profiles):
            self.show_profile(p, i)

    def get_profile(self, ssid="", passwd=""):
        profile = pywifi.Profile()
        profile.ssid = ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = passwd
        return profile

    def connect_by_profile(self, profile, timeout=10):
        self.iface.disconnect()
        # connecting
        profile = self.iface.add_network_profile(profile)
        self.iface.connect(profile)
        ret = False
        for i in range(timeout):
            if self.iface.status() == const.IFACE_CONNECTED:
                ret = True
                break
            else:
                time.sleep(1)
        return ret

    def connect(self):
        ssid = "Xiaomi 13 Pro"
        passwd = "12345679"
        profile = self.get_profile(ssid, passed)
        if (self.connect_by_profile(profile) == True):
            print("connect to %s success!"% (ssid))
        else:
            print("connect to %s failed!"% (passwd))

if __name__ == '__main__':
    wifi = WiFi()
    wifi.scan_wifi()
    wifi.connect()


