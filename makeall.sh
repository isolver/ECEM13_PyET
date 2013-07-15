make html
make latexpdf
mv ./build/latex/*.pdf ./build/html/
rsync -r build/html/ /Volumes/www/staff/jwp/P4N