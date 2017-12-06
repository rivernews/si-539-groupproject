git fetch upstream
git merge upstream/master
git checkout team-edit
git add .
git commit -m "Sync With Upstream by script"
git push origin team-edit