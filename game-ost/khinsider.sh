# automates the ost download from khinsider
# khinsider is the video game ost collection

# requires wget installed 

wget_installed=`which wget;echo $?`

if [ "$wget_installed" == 0 ]; then
    echo "please install wget"
    exit 0
fi
    
htmlFiles=`curl $1|grep $1|cut -d \" -f 2 `
mkdir $1 
cd $1
touch level2.txt
for f in $htmlFiles
do
    l=`curl $f|grep "<audio"|cut -d \" -f 4`
    if ! grep -Fxq $l level2.txt
    then
        echo $l >> level2.txt
    fi
done
files=`cat level2.txt`
rm level2.txt
for f in $files
do
    wget $f
done

# sends notification in mac
# osascript -e 'display notification "download finished" with title "'$1'"'

# sends notification in gnome
# notify-send "download finished" $1
