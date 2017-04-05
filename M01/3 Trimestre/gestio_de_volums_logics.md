## Gestió de Volums Lògics
+ #####  Què són?
    -Són una capa d'extracció entre dispositius d'emmagatzematge i un sistema de fitxers. Tambè és anomenat Logical Volume Manager (LVM).
* ##### Què volen dir les sigles, definició, analogies i exemples de comandes (explicant què fan) vistes a classe de:
    __PV:__

    -Aquestes sigles volen dir Physical Volume (Volum Físic).

    -És un dispositiu d'emmagatzematge o, més ben dit, un dispositiu de blocs.

    -Podria ser un Disc Dur, una partició, una targeta SD, un floppy, un dispositiu RAID, un dispositiu loop, un dispositiu de xifrat o inclós un Volumen Lògic (LV).
    
        pvcreate /dev/vda → Crea un Physical Volume del Disc Dur /dev/vda.
    
        pvs → Veure els Volums Físics que hi tenim al nostre PC.
    
    
    __VG:__
    
    -Aquestes sigles volen dir Volume Group (Volum de Grup).
    
    -Es podria dir que VG és una espècie de disc dur virtual. Està compost d'un o més PVs.
    
    -És la "caixa" en la que tenim les nostres Volums Lògics (LV) i els nostres Volums Físics (PV)
    
        vgcreate multimedia /dev/vda → Crea un Volume Group
        
        vgs → Veure els Volums de Grup que hi tenim al PC.
    
    
    __LV:__
    
    -Aquestes sigles volen dir Logical Volume (Volum Lògic).
    
    
