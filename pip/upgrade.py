#Script to upgrade all packages
for i in $(pip list -o | awk 'NR > 2 {print $1}'); do sudo pip install -U $i; done
