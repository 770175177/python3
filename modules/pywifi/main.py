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
        self.old_profiles = self.iface.network_profiles()
        self.results = []
        self.types = {}
        const_attrs = dir(const)
        constants = [attr for attr in const_attrs if attr.isupper()]
        self.types['IFACE_STATUS'] = {getattr(const, k): k for k in constants if 'IFACE' in k}
        self.types['AKM_TYPE'] = {getattr(const, k): k for k in constants if 'AKM_TYPE' in k}
        self.types['AUTH_ALG'] = {getattr(const, k): k for k in constants if 'AUTH_ALG' in k}
        self.types['CIPHER_TYPE'] = {getattr(const, k): k for k in constants if 'CIPHER_TYPE' in k}
        self.types['KEY_TYPE'] = {getattr(const, k): k for k in constants if 'KEY_TYPE' in k}
        print("wifi init done, iface[0] status %s!"% (self.types['IFACE_STATUS'][self.iface.status()]))

    def scan_wifi(self, show=True):
        print("scaning wifi...")
        self.iface.scan()                       # start scan
        time.sleep(2)                           # ensure scan done
        results = self.iface.scan_results()     # get scaned wifi list
        self.results = sorted(results, key=lambda x: x.signal, reverse=True)
        for i, result in enumerate(self.results):
            bssid = result.bssid
            if result.signal < -80:
                self.results.remove(result)
            elif show == True:
                self.show_profile(result, i)

    def show_profile(self, profile, index=0):
        if profile is None:
            return
        print("\n[%2d] ssid: %s"% (index, profile.ssid))
        if hasattr(profile, 'signal'):
            print("\tsignal: %d"% (profile.signal))
        if hasattr(profile, 'freq'):
            print("\tfreq  : %.2f GHz (%d Hz)"% (profile.freq/1024/1024, profile.freq))
        if type(profile.akm) == int:
            print("\takm   : %s"% (self.types['AKM_TYPE'][profile.akm]))
        else:
            print("\takm   :", end='')
            for i, akm in enumerate(profile.akm):
                print("%s%s"% (' ' if not i else '\t'+' '*8, self.types['AKM_TYPE'][akm]))
        if type(profile.auth) == int:
            print("\tauth  : %s"% (self.types['AUTH_ALG'][profile.auth]))
        else:
            print("\tauth  :", end='')
            for i, auth in enumerate(profile.auth):
                print("%s%s"% (' ' if not i else '\t'+' '*8, self.types['AUTH_ALG'][auth]))
        print("\tcipher: %s"% self.types['CIPHER_TYPE'][profile.cipher])
        print("\tbssid : %s"% profile.bssid)
        print("\tkey   : %s"% profile.key)

    def show_connected_profiles(self):
        for i, p in enumerate(self.old_profiles):
            self.show_profile(p, i)

    def gen_profile_by_passwd(self, ssid="", passwd=""):
        profile = pywifi.Profile()
        profile.ssid = ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = passwd
        return profile

    def get_scaned_profile_by_ssid(self, ssid):
        if not self.results:
            print("scaned list is empty, please scan wifi!")
        for profile in self.results:
            if (ssid == profile.ssid):
                print("get scaned profile ssid: %s"% (ssid))
                return profile
        print("can't find the ssid of %s in scaned list!"% (ssid))
        return None

    def set_passwd_to_profile(self, profile, passwd):
        if profile:
            profile.key = passwd
        return profile

    def connect_by_profile(self, profile, timeout=10):
        if self.iface.status() != const.IFACE_DISCONNECTED:
            self.iface.disconnect()
        # remove old profile
        for i, old_profile in enumerate(self.old_profiles):
            if profile.ssid == old_profile.ssid:
                print("old %s profile exist, remove it"% (profile.ssid))
                self.iface.remove_network_profile(old_profile)
                self.old_profiles.remove(old_profile)
        # connecting
        if not self.get_scaned_profile_by_ssid(profile.ssid):
            profile = self.iface.add_network_profile(profile)
        self.iface.connect(profile)
        for i in range(timeout):
            if self.iface.status() == const.IFACE_CONNECTED:
                print("connected to wifi %s"% (profile.ssid))
                return True
            else:
                print("\rtry to connect to wifi %s %d times"% (profile.ssid, i), end='', flush=True)
                time.sleep(1)
        print("\ncan't connect to wifi %s"% (profile.ssid))
        return False

    def connect(self):
        # profile = self.gen_profile_by_passwd(ssid, passwd)
        profile = self.get_scaned_profile_by_ssid("Xiaomi 13 Pro")
        profile = self.set_passwd_to_profile(profile, "12345679")
        self.show_profile(profile)
        self.connect_by_profile(profile)

if __name__ == '__main__':
    wifi = WiFi()
    wifi.scan_wifi(show=False)
    wifi.connect()


