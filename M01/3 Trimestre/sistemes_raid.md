# M01-Hardware
# Sistemes RAID

1. Resum de sistemes RAID fent servir una taula com la vista a classe.

| RAID'S | Nº Mínim discs | Nº Mínim discs fallats | Capacitat | Read | Write |
| :----: | :------------: | :--------------------: | :-------: | :--: | :---: |
| RAID 0 | 2 | 0 | 100 % | E | E |
| RAID 1 | 2 (Màx.) | 1 | 50 % | VG | G |
| RAID 5 | 3 | 1 | 67 - 94 % | VG | G |
| RAID 6 | 4 | 2 | 50 - 88 % | G | G |
| RAID 10 | 4 | 1 de cada mirror | 50 % | VG | G |

2. Descripció de la metodologia utilitzada a classe per a fer proves amb màquines virtuals.
	1. 	Creem la maquina virtual 
	2.	Creem 3 discs (200MB cada un)
	3.	Ens posem com a root
	4.	Executem la comanda **mdadm**
	5. 	**mdadm --create < nom dispositiu> --level=<raid que volguis> --raid-devices=<nº de discs> <disc1> <disc2>**
	6.	Quedaria així: mdadm -- create /dev/md0 --level=1 --raid-devices=2 /dev/vda /dev/vdb
	7.	**cat /proc/mdstat** (fitxer on tenim l'estat del raid)
	8.	mkfs.ext4 /dev/md0
	9.	mount /dev/md0 /mnt
	10.	cd /mnt
	11.	dd if= /dev/cero of=test.img bs=4k count=1000
	12.	ls -lh
	13.	less test.img
	
3. Comandes i descripció de les mateixes per tal de crear un sistema RAID1
	
	+ mdadm --create < nom dispositiu> --level=<raid que vulguis> --raid-devices=<nº de discs> <disc1> <disc2>
	+ mdadm -- create /dev/md0 --level=1 --raid-devices=2 /dev/vda /dev/vdb
	
4. Comandes i descripció de les mateixes per tal de crear un sistema RAID5

	+ mdadm --create < nom dispositiu> --level=<raid que vulguis> --raid-devices=<nº de discs> <disc1> <disc2> <disc3>
	+ mdadm -- create /dev/md0 --level=5 --raid-devices=3 /dev/vda /dev/vdb /dev/vdc

5. Comandes i descripció de les mateixes per tal de crear un sistema RAID6
	
	+ mdadm --create < nom dispositiu> --level=<raid que vulguis> --raid-devices=<nº de discs> <disc1> <disc2> <disc3> <disc4> 
	+ mdadm -- create /dev/md0 --level=6 --raid-devices=4 /dev/vda /dev/vdb /dev/vdc /dev/vdd

6. Comandes i descripció de les mateixes per tal de crear un sistema RAID10
	
	+ mdadm --create < nom dispositiu> --level=<raid que vulguis> --raid-devices=<nº de discs> <disc1> <disc2> <disc3> <disc4>
	+ mdadm -- create /dev/md0 --level=10 --raid-devices=4 /dev/vda /dev/vdb /dev/vdc /dev/vdd














