
function runEnv {
	echo "Running Enviroment"
	source env/bin/activate
}


function setupEnv {
	type virtualenv &>/dev/null || sudo pip install virtualenv
	virtualenv --version
	python3 -m venv env
	checkDependencies
}

function checkDependencies {
	runEnv
	pip install --upgrade pip
	pip install -r requirements.txt
}

function runTest {
	runEnv
	echo "testing: Not Really Part to be Implemented"
}

function updateEnv {
	runEnv
	pip freeze > requirements.txt
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

case "$1" in
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

esac