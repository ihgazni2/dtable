pip3 uninstall dtable
git rm -r dist
git rm -r build
git rm -r dtable.egg-info
rm -r dist
rm -r build
rm -r dtable.egg-info
git add .
git commit -m "remove old build"

