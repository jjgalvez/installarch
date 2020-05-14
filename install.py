from subprocess import run
 
basepkgs = ' '.join([
    'base', 
    'linux', 
    'linux-lts', 
    'linux-firmware',
    'networkmanager', 
    'nano', 
    'man-db', 
    'man-pages', 
    'less', 
    'texinfo',
    'base-devel'
])

gnome = ' '.join([
    'gnome',
    'gnome-extra',
    'gnome-shell-extensions'
])

otherpkgs = ' '.join([
    'firefox'
])


def runCMD(cmd):
    out = run(cmd, shell=True, capture_output=True, text=True)
    if out.returncode == 0:
        return out
    else:
        return False


def printCMDOutput(cmd):
    if out := runCMD(cmd):
        print(out.stdout)
    else:
        print('Error')



# EFI or BIOS
print('EFI') if runCMD('ls /sys/firmware/efi/efivars') else print('BIOS')

# update system clock
print('Updating system clock')
runCMD('timedatectl set-ntp true')

#format disk
print('disk info')
printCMDOutput('fdisk -l')
run('gdisk', shell=True)
printCMDOutput('fdisk -l')
print('format disks')
if swap := input('enter swapt Partition: ').strip():
    printCMDOutput(f'mkswap {swap}')
if root := input('enter root Partition: ').strip():
    printCMDOutput(f'mkfs.ext4 {root}')

print('Mount root')
runCMD(f'mount {root} /mnt')

print('pacstrap base')
run(f'pacstrap /mnt {basepkgs}', shell=True)

print('pacstrap gnome')
run(f'pacstrap /mnt {gnome}', shell=True)

print('pacstrap other packages')
run(f'pacstrap /mnt {otherpkgs}')


