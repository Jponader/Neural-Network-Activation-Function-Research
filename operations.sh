function runEnv {
	echo "Running Enviroment"
	source env/bin/activate
}

function install {
	echo "Python3 Virtual Enviroment needs to be installed"
	read -p "Would you like us to install it??  Y or N" -n 1 -r
	echo '\n'
	if [[ ! $REPLY =~ ^[Yy]$ ]]
	then
	    exit 1
	fi
}

function installPython {
	echo "Please Install Python3 onto the System to proceed"
	echo "Python 3.7 is Recomended"
	ech0 "Linux: apt install python3"

	exit 1
}

function installPip {
	echo "Please Install Pip3 onto the System to proceed"
	ech0 "Linux: apt install pip3"

	exit 1
}

function checkEnviromnet {
	echo "Checking System"
	type python3 &>/dev/null || installPython
	type pip3 &>/dev/null || installPip
	type virtualenv &>/dev/null || installCheck "virtualenv"
	type virtualenv &>/dev/null || pip3 install virtualenv
	echo "Sytem Check Complete, System ready to go"
	echo ""
	echo "To Setup Enviroment"
	echo "	./openML.sh --setupEnv"
}


function setupEnv {
	checkEnviromnet
	python3 -m venv env
	checkDependencies
}

function checkDependencies {
	runEnv
	pip3 install --upgrade pip
	pip3 install -r requirements.txt
}

function runTest {
	runEnv
	python3 tester.py
}

function updateEnv {
	runEnv
	pip3 freeze > requirements.txt
}

function run() {
	runEnv
	if [ -z $1 ] 
		then 
			echo "Please Include Python file to Run"
			echo "./operations.sh --runPY <file>.py"
		else
			echo "Running" $1
			python3 $1
	fi
}

function board(){
	runEnv
	if [ -z $1 ] 
		then 
			echo "Please Include Python file to Run"
			echo "./operations.sh --tensorboard <log File Dir>"
		else
			tensorboard --logdir $1
	fi
	
}

case "$1" in

	"--check")
		checkEnviromnet
		;;

	"--setupEnv")
		setupEnv
		;;

	"--runTest")
		runTest
		;;

	"--Requpdate")
		updateEnv
		;;

	"--update")
		checkDependencies
		;;

	"--runPY")
		shift
		run $1
		;;

	"--tensorboard")
		shift
		board $1
		;;

	"")
		echo "To test enviroment:"
		echo "	operations.sh --check"

esac