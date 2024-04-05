# robinhood-operator
A Kubernetes based Operator to automatically trade Stocks and Options on Robinhood....cause why not

### Run Locally
kopf run src/operator/operator.py

### Virtual env for operator
# from root
virtualenv venv --system-site-packages
source ./venv/bin/activate
pip install -r requirements.txt

### Virtual env for algo/equity
cd algos/equity
virtualenv venv --system-site-packages
source ./venv/bin/activate
pip install -r requirements.txt