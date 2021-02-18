#!/bin/bash

docker run --rm \
  -e COUNTY="Netherlands" \
  -e STATE="Zuid-Holland" \
  -e LOCATION="Rotterdam" \
  -e ORGANISATION="Payter B.V." \
  -e ISSUER_CN="Payter B.V. DevOps team" \
  -e PUBLIC_CN="please give an url" \
  -e ISSUER_NAME="Payter B.V." \
  -e PUBLIC_NAME="Payter B.V." \
  -v hobbit:/etc/ssl/certs \
  pgarrett/openssl-alpine