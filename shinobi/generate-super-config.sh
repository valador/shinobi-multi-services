#!/bin/sh

set -euf -o pipefail
#под кубернет генерация хэша не пригодится
#PASSWORD_HASH="$(echo -n "${SHINOBI_SUPER_USER_PASSWORD}" | md5sum | sed -e 's/  -$//')"
PASSWORD_HASH="$(echo -n "${SHINOBI_SUPER_USER_PASSWORD}" | openssl dgst -sha256 | sed -e 's/^.* //')"

configDestination="${SHINOBI_INSTALL_DIRECTORY}/super.json"

jq -n "[.mail=\"${SHINOBI_SUPER_USER_EMAIL}\" | .pass=\"${PASSWORD_HASH}\" | .tokens=[\"${SHINOBI_SUPER_USER_TOKEN}\"]]" \
    > "${configDestination}"

>&2 echo "Generated Shinobi super configuration: ${configDestination}"
