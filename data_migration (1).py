from datetime import datetime
now = datetime.now()
m_type = True
source_true = True
target_true = True
nbk_true = True
solo_true = True
exit_true = False

boa_number = input('Enter BOA number including the letters BOA: ') #Asks for the BOA ticket number
boa_cap = boa_number[0:3].upper() + boa_number[3:] #capitalizes "BOA"
boa_time = input('Enter time the ticket started (leave blank if unknown): ') #Asks for time started
tech_name = input('Enter assigned technician\'s name: ') #Asks for the tech's name
tech_email = input('Enter technician\'s email: ') #Asks for the tech's email
email_lower = tech_email.lower() #lower cases the email address

#determines if this is a migration or backup, and loops if neither 1 or 2 are chosen
while m_type == True:
    bam_type = input('Migration type? "1" for migration, "2" for backup\\reimage: ')
    if (bam_type != '1' and bam_type != '2'):
        print('Please select 1 or 2.')
    else:
        m_type = False

#Asks for the source name, and loops if left blank
while source_true == True:
    source_pc = input('Enter the source PC name: ') 
    if len(source_pc) == 0:
        print('Source PC cannot be blank.')
    else:
        cap_source = source_pc.upper()
        source_true = False

source_ip = input('Enter the source IP (leave blank if unknown): ') #Asks for the Source IP if known. Field may be left blank.

#Asks for the target name, and loops if left blank. This only occurs if this is a migration and not a backup.
if bam_type == '1':
    while target_true == True:
        target_pc = input('Enter the target PC name: ')
        if len(target_pc) == 0:
            print('Target PC cannot be blank.')
        else:
            cap_target = target_pc.upper()
            target_true = False
    target_ip = input('Enter the target IP (leave blank if unknown): ') #Asks for the Target IP if known. Field may be left blank.

#Asks whether only 1 NBK needs to be migrated or backed up. If there is, the user ID field cannot be blank.
while nbk_true == True:
    nbk_req = input('Was only 1 user ID requested for the migration? [Y/N]: ')
    if nbk_req.upper() == 'Y':
        while solo_true == True:
            solo_nbk = input('Please type the user ID requested: ')
            if len(solo_nbk) == 0:
                print('user ID cannot be blank.')
            else:
                cap_solo = solo_nbk.upper()
                solo_true = False
        nbk_true = False
    elif nbk_req.upper() == 'N':
        nbk_true = False
    else:
        print('Please type Y or N.')

#verbiage for the BOA ticket
print()
print()
print('TICKET VERBIAGE')
print('**WSS AGENT TIME ACCOUNTING**')
print('Agent Name: David Hu')
print('Date ' + str(now.month) + '//' + str(now.day) + '//' + str(now.year)) #prints today's date
print()

#prints ticket verbiage, depending on the migration type
if bam_type == '1':
    print('Data migration started by David Hu.')
else:
    print('Data backup started by David Hu.')
print('source: ' + cap_source)
if bam_type == '1':
    print('target: ' + cap_target)
print()

if len(boa_time) == 0:
    print('Time Start: X:XX AM')
else:
    print('Time Start: ' + boa_time)
print('Time End: X:XX AM',)
print('************************')

#verbiage for the personal email
print('EMAIL VERBIAGE')
print()
if bam_type == '1':
    print('SUBJECT: ' + boa_cap + ' Data Migration')
else:
    print('SUBJECT: ' + boa_cap + ' Backup & Reimage')
print('Tech: ' + tech_name + ' (' + email_lower + ')')
print('Source: ' + cap_source)

if bam_type == '1':
    print('Target: ' + cap_target)

if nbk_req.upper() == 'Y':
    print('User ID: ' + cap_solo)
print('************************')

#verbiage for the Sticky Note on your bank laptop
print('BANK STICKY NOTE VERBIAGE')
print()
if bam_type == '1':
    print(boa_cap + ' (' + tech_name + ') (' + email_lower + ')')
else:
    print(boa_cap + ' Backup & Reimage (' + tech_name + ') (' + email_lower + ')')

if len(source_ip) == 0:
    print('Source: ' + cap_source)
else:
    print('Source: ' + cap_source + ' (' + source_ip + ')')

if bam_type == '1':
    if len(target_ip) == 0:
        print('Target: ' + cap_target)
    else:
        print('Target: ' + cap_target + ' (' + target_ip + ')')

if nbk_req.upper() == 'Y':
    print('User ID: ' + cap_solo)

#Window does not close until a key is pressed
while exit_true == False:
    exit_input = input('Type EXIT to quit: ')
    if exit_input.upper() == 'EXIT':
        exit_true = True