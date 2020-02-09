curl -i -s -k -X $'POST' -H $'Host: domain.careers' --data-binary $'username=ghost' $'http://domain.careers/recovery' | grep "Sent recovery password to"
curl -i -s -k -X $'POST' -H $'Host: domain.careers' --data-binary $'username=admin' $'http://domain.careers/recovery' | grep "Sent recovery password to"
curl -i -s -k -X $'POST' -H $'Host: domain.careers' --data-binary $'username=ghost1' $'http://domain.careers/recovery' | grep "Sent recovery password to"
