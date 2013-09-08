import usb.core
import usb.util
import usb.control


def captureLauncher( reqVendor =0x1130, reqProduct = 0x0202):
    dev = usb.core.find(idVendor=reqVendor, idProduct=reqProduct)
    if dev is None:
        print "Shit huh"
        return dev
    dev.set_configuration()
    # get an endpoint instance
    cfg = dev.get_active_configuration()
    interface_number = cfg[(0,0)].bInterfaceNumber
    alternate_setting = usb.control.get_interface(interface_number)
    intf = usb.util.find_descriptor(
        cfg, bInterfaceNumber = interface_number,
        bAlternateSetting = alternate_setting
    )
    
    ep = usb.util.find_descriptor(
        intf,
        # match the first OUT endpoint
        custom_match = \
        lambda e: \
            usb.util.endpoint_direction(e.bEndpointAddress) == \
            usb.util.ENDPOINT_OUT
    )
    return ep
    
    
    
#def oldCapture( reqVendor =0x1130, reqProduct = 0x0202):
#    for i, bus in enumerate(busses()):
#        devices = bus.devices
#        for j, device in enumerate(devices):
#            if device.idVendor == reqVendor:
#                if device.idProduct == reqProduct:
#                    print "Yay"
#                    #this next part is cheating and I have no idea whether it is 100% valid
#                    for i, config in enumerate(device.configurations): 
#                        for j, interface in enumerate(config.interfaces):
#                            for k, nest_inter in enumerate(interface):   
#                                handle = device.open()
#                                handle.claimInterface(nest_inter)
#                                return handle

device = captureLauncher()
first=0x5553424300000400 #usb capture proves this comes first
second=0x5553424300400200 #then this - dunno why
# this should turn the USB device left
left=0x00010000000008080000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
while True:
    device.ctrl_transfer(0x21,0x09,0x01,0x0200,first);
    device.ctrl_transfer(0x21,0x09,0x01,0x0200,second);
    device.ctrl_transfer(0x21,0x09,0x00,0x0200,left);