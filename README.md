# Haveibeenpwn-script
- haveibeenpwn.py: Simple python script to find pwned emails with a nickname

Usage:

./haveibeenpwn.py mynickname

the script will test the username with a list of providers
used for this article: http://blog.mathieuchot-plassot.com/personal-vendetta-data-breach-investigation/
------------------------------------------------------------------------------------------------------------
# Advanced generator
-mail-generator.py: Simple mail generator/checker with mutiple arguments for haveibeenpwn.com

./mailgenerator.py -f 'mathieu' -l 'chot-plassot' -s '1337' -p 'protonmail.com'

This script generate an advanced list of emails and check if those emails have been pwned on haveibeenpwn.com
