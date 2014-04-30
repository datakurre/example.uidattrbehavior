#!/bin/bash

bin/i18ndude rebuild-pot --pot src/example/uidattrbehavior/locales/example.uidattrbehavior.pot --merge src/example/uidattrbehavior/locales/manual.pot --create example.uidattrbehavior src/example/uidattrbehavior

bin/i18ndude sync --pot src/example/uidattrbehavior/locales/example.uidattrbehavior.pot src/example/uidattrbehavior/locales/*/LC_MESSAGES/example.uidattrbehavior.po
