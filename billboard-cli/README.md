## billboard 
crawls through the billboard top 100 chart

### options
	
    -x       displays first x number of songs (x being integer)     
    -sw      sort by weeks                                          
    -sr      sort by rank                                          
    -t       explicitly display title                           
    -n       explicitly display the rank ( number )            
    -a       explicitly display the artist name                
    -w       explicitly display the week on chart             


###### adding it to your bash shell

        git clone https://github.com/AkhilMaskery/bBoard.git  

        cd bBoard.git 
        
        pip install requests lxml bs4 colorama 

        echo alias bboard='python $PWD/billboard.py' >> ~/.bashrc 

###### or install it by this one liner

        curl https://raw.githubusercontent.com/AkhilMaskery/bBoard/master/install.sh | sh
