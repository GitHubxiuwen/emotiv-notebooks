# !/bin/bash
OS=$(lsb_release -s -i)
if [ "${OS}" = "Ubuntu" ]
then
	echo "Checking internet connectivity..."
	ping -c 5 www.emotiv.com>>/dev/null

	EDITION="Research"
	EDITIONDIR="EmotivResearch_2.0.0.20"
	VERSION="2.0.0.20"

	if [ $? -eq  0 ]
	then
		sudo apt-get install wget libudev-dev libxtst-dev libx11-dev libxext-dev python-qt4 libjpeg62

		rm -rf /home/$USER/$EDITIONDIR
		mkdir /home/$USER/$EDITIONDIR

		cd /home/$USER/$EDITIONDIR

		#wget -O Install.py "http://emotiv.com/linuxdeployment/download_test.php?filename=Install.py"
		#wget -O backgroud.png "http://emotiv.com/linuxdeployment/download_test.php?filename=backgroud.png"
		#wget -O emotiv_consumer.png "http://emotiv.com/linuxdeployment/download_test.php?filename=emotiv_consumer.png"

		sed -i "s/thayeditionvaoday/$EDITION/" Install.py
		sed -i "s/thayversionvaoday/$VERSION/" Install.py

		sudo python Install.py

		rm Install.py
		rm backgroud.png
		rm emotiv_consumer.png
	else
		echo "Please check your internet connecton!"
	fi
else
	echo "Checking internet connectivity..."
	ping -c 5 www.emotiv.com>>/dev/null

	EDITION="Research"
	EDITIONDIR="EmotivResearch_2.0.0.20"
	VERSION="2.0.0.20"

	if [ $? -eq  0 ]
	then
		su -c 'yum install wget libudev-devel libXtst-devel libX11-devel libXext-devel zenity PyQt4'

		rm -rf /home/$USER/$EDITIONDIR
		mkdir /home/$USER/$EDITIONDIR

		cd /home/$USER/$EDITIONDIR

		#wget -O Install.py "http://emotiv.com/linuxdeployment/download_test.php?filename=Install.py"
		#wget -O backgroud.png "http://emotiv.com/linuxdeployment/download_test.php?filename=backgroud.png"
		#wget -O emotiv_consumer.png "http://emotiv.com/linuxdeployment/download_test.php?filename=emotiv_consumer.png"

		BACKUPDBUSSESSION=$DBUS_SESSION_BUS_ADDRESS
		unset DBUS_SESSION_BUS_ADDRESS
		echo $USER

		sed -i "s/thayeditionvaoday/$EDITION/" Install.py
		sed -i "s/thayversionvaoday/$VERSION/" Install.py

		su -c "python Install.py"

		rm Install.py
		rm backgroud.png
		rm emotiv_consumer.png
		DBUS_SESSION_BUS_ADDRESS=$BACKUPDBUSSESSION
		set DBUS_SESSION_BUS_ADDRESS
	else
		echo "Please check your internet connecton!"
	fi
fi
