#!/bin/bash

docker run --rm \
 -e OPENSSL_V110="${HOME}/local/bin/openssl.sh"
 -e PUB_WRAPPING_KEY="${HOME}/wrapping-key.pem"
 -e TARGET_KEY=/path/to/key
 -e BASE_DIR="${HOME}/wrap_tmp"
 -e mkdir -m 700 -p ${BASE_DIR}


 -e TEMP_AES_KEY="${BASE_DIR}/temp_aes_key.bin"
 -e TEMP_AES_KEY_WRAPPED="${BASE_DIR}/temp_aes_key_wrapped.bin"
 -e TARGET_KEY_WRAPPED="${BASE_DIR}/target_key_wrapped.bin"

 -e RSA_AES_WRAPPED_KEY=/path/to/wrapped-target-key.bin
 -e mkdir -m u+wx -p $(dirname ${RSA_AES_WRAPPED_KEY})

#generatethekey

 -e "${OPENSSL_V110}" rand -out "${TEMP_AES_KEY}" 32

#wrapthekey
 
 -e "${OPENSSL_V110}" rsautl \
   -encrypt \
   -pubin \
   -inkey "${PUB_WRAPPING_KEY}" \
   -in "${TEMP_AES_KEY}" \
   -out "${TEMP_AES_KEY_WRAPPED}" \
   -oaep

 -e "${OPENSSL_V110}" enc \
 -e -id-aes256-wrap-pad \
 -e -iv A65959A6 \
 -e -K $( hexdump -v -e '/1 "%02x"' < "${TEMP_AES_KEY}" ) \
 -e -in "${TARGET_KEY}" \
 -e -out "${TARGET_KEY_WRAPPED}"
   pgarrett/openssl-alpine

