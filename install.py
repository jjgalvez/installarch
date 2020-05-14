from subprocess import run

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

#print disk info
print('disk info')
printCMDOutput('fdisk -l')
