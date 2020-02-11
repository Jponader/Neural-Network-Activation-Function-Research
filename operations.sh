
function runEnv {
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
	pip install -r requirements.txt
}

function runTest {
	runEnv
	echo "testing"
}

function updateEnv {
	runEnv
	pip freeze > requirements.txt
}

case "$1" in
	"--setupEnv")
		setupEnv
		;;

	"--runTest")
		runTest
		;;

	"--update")
		updateEnv
		;;

	"--checkupdate")
		checkDependencies
		;;

esac