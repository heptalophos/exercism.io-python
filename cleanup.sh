#!/usr/bin/env bash
exec 2> /dev/null

rm -r ./*/__pycache__ && echo "Removed all __pycache__s" || echo "There are no __pycache__ directories to remove"
rm -r ./*/.pytest_cache/ && echo "Removed all .pytest_caches" || echo "There are no .pytest_cache directories to remove"

echo ==================================
echo Done!!