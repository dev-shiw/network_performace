import platform
import psutil
import cpuinfo
import wmi
#system and hardware information

print(f"architecture:{platform.architecture()}")
print(f"network name:{platform.node()}")
print(f"operating system:{platform.platform()}")
print(f"processor:{platform.processor()}")

my_cpuinfo= cpuinfo.get_cpu_info()
print(f"full cpu name:{my_cpuinfo['brand_raw']}")
print(f"freq(hz actual):{my_cpuinfo['hz_actual_friendly']}")
print(f"freq(hz advertised):{my_cpuinfo['hz_advertised_friendly']}")
print(f"total ram: {psutil.virtual_memory().total/1024/1024/1024:.2f} gb")
print(f" free: {psutil.virtual_memory().free/1024/1024/1024:.1f} gb")
#prints all the cpu info
#print(my_cpuinfo)
#print(my_cpuinfo.keys())

pc=wmi.WMI()
os_info=pc.Win32_OperatingSystem()[0]
print(os_info)
print(pc.Win32_Processor()[0].name)
print(pc.Win32_VideoCOntroller()[0].name)
#print(pc.Win32_VideoCOntroller()[0])
