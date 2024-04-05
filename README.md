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


### Helmfile
# You will need to create a file with the secrets
touch helm/operator.secrets.gotmpl
# The file contents should look like
# The MFA OTP must be configured in Robinhood. Docs here: https://robin-stocks.readthedocs.io/en/latest/quickstart.html#:~:text=NOTE%3A%20to%20use,your%20robinhood%20app.
```
secrets:
  ROBINHOOD_USERNAME: <Robinhood Username>
  ROBINHOOD_PASSWORD: <Robinhood Password>
  ROBINHOOD_OTP: <MFA OTP>
  ```

cd helm
helmfile template
helmfile sync