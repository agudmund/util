#!/bin/bash

openssl genrsa -out priv.key 1024
openssl req -new -key priv.key -out server.crt -x509 -days 365