#!/bin/bash

OriginVSDKDirectory=codegen/3.1/vsdk
DestinationVSDKDirectory=vsdk

AutogeneratesDirectory=autogenerates
FetchersDirectory=fetchers

AutogeneratesFiles=('nudomain.py' 'nuenterprise.py' 'nurestuser.py')
FetchersFiles=('nudomains_fetcher.py')
VSDKFiles=('constants.py' 'nunsgateway.py')

copy_files ()
{
    declare -a filenames=("${!1}")
    for filename in ${filenames[@]}; do
        echo "Updating $3/$filename"
        cp $2/$filename $3
    done
}

generate-vspk -f V3_1/

copy_files AutogeneratesFiles[@] "$OriginVSDKDirectory/$AutogeneratesDirectory" "$DestinationVSDKDirectory/$AutogeneratesDirectory"
copy_files FetchersFiles[@] "$OriginVSDKDirectory/$FetchersDirectory" "$DestinationVSDKDirectory/$FetchersDirectory"
copy_files VSDKFiles[@] "$OriginVSDKDirectory" "$DestinationVSDKDirectory"

rm -rf codegen
